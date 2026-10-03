#!/usr/bin/env python3
"""Aggregate only declared comparable observations; descriptive domain means are optional."""

import argparse
import json
import math
import statistics
import sys
from collections import defaultdict

KEYS=("model","effort","benchmark","dataset_version","metric","unit","protocol","surface","evaluator","tool_config","evidence_status")
VALID_EFFORTS={"none","low","medium","high","xhigh","max","unknown"}

def aggregate(data):
    rows=data.get("observations")
    if not isinstance(rows,list):
        raise ValueError("observations must be a list")
    seen={}
    groups=defaultdict(list)
    missing=[]
    for row in rows:
        if not isinstance(row,dict):
            raise ValueError("observation must be an object")
        for key in (*KEYS,"observation_id","source_url","retrieved_at"):
            if not isinstance(row.get(key),str) or not row[key].strip():
                raise ValueError(f"missing/non-string {key}")
        if row["effort"] not in VALID_EFFORTS:
            raise ValueError("invalid effort")
        ident=row["observation_id"]
        if ident in seen:
            if row!=seen[ident]:
                raise ValueError(f"conflicting duplicate observation: {ident}")
            continue
        seen[ident]=row
        value=row.get("value")
        if value is None:
            missing.append(ident)
            continue
        if type(value) not in (float,int) or not math.isfinite(value):
            raise ValueError("score must be finite number or null")
        if row["unit"]=="percent" and not 0<=value<=100:
            raise ValueError("percent out of range")
        if row["unit"]=="signed_index" and not -100<=value<=100:
            raise ValueError("signed_index out of range")
        if row["unit"]=="usd_per_task" and value<0:
            raise ValueError("negative cost")
        key=tuple(row[k] for k in KEYS)
        if any("unknown" in row[k].lower() or "not_reported" in row[k].lower()
               for k in ("dataset_version","protocol","surface","evaluator","tool_config")):
            key+=(row["observation_id"],)
        groups[key].append(row)

    results=[]
    for vals in groups.values():
        experiments=[r.get("experiment_id",r["observation_id"]) for r in vals]
        if len(set(experiments))!=len(experiments):
            raise ValueError("same experiment counted more than once")
        record={k:vals[0][k] for k in KEYS}
        numbers=[r["value"] for r in vals]
        record.update(
            mean=statistics.mean(numbers),
            n_observations=len(numbers),
            min=min(numbers),
            max=max(numbers),
            sample_sd=statistics.stdev(numbers) if len(numbers)>1 else None,
            confidence_interval=None,
            source_observations=[r["observation_id"] for r in vals],
            interpretation="single_published_observation" if len(numbers)==1 else "mean_of_matched_runs_not_pooled_accuracy",
        )
        results.append(record)

    domains=[]
    for definition in data.get("domains",[]):
        members=definition["benchmarks"]
        if not members or len(members)!=len(set(members)):
            raise ValueError("domain members must be nonempty and unique")
        configs=sorted(set((r["model"],r["effort"]) for r in results))
        for model,effort in configs:
            selected=[]
            for bench in members:
                hits=[r for r in results if r["model"]==model and r["effort"]==effort and r["benchmark"]==bench and r["unit"]=="percent" and r["evidence_status"]=="published_reported"]
                if len(hits)>1:
                    raise ValueError("multiple protocol groups: choose a dataset slice before domain averaging")
                if hits:
                    selected.extend(hits)
            compatible=len({(r["evaluator"],r["surface"],r["tool_config"]) for r in selected})<=1
            full=len(selected)==len(members) and compatible
            domains.append({
                "model":model,
                "effort":effort,
                "standard":definition["name"],
                "macro_mean":statistics.mean(r["mean"] for r in selected) if full else None,
                "coverage":f"{len(selected)}/{len(members)}",
                "included":[r["benchmark"] for r in selected],
                "status":"descriptive_equal_benchmark_weight" if full else "INSUFFICIENT_COMPARABLE_COVERAGE",
                "is_success_probability":False,
            })

    return {
        "schema_version":"1.0",
        "standard_results":results,
        "domain_results":domains,
        "missing_observations":missing,
        "deduplicated_count":len(rows)-len(seen),
        "warning":"No global rank. Published summaries lack run-level uncertainty; null is not zero.",
    }

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input")
    parser.add_argument("--output")
    args=parser.parse_args()
    try:
        with open(args.input,encoding="utf-8") as fh:
            result=aggregate(json.load(fh))
        rendered=json.dumps(result,ensure_ascii=False,indent=2,allow_nan=False)+"\n"
        if args.output:
            with open(args.output,"w",encoding="utf-8") as fh:
                fh.write(rendered)
        else:
            print(rendered,end="")
        return 0
    except (OSError,ValueError,TypeError,KeyError) as exc:
        print(json.dumps({"error":str(exc)}),file=sys.stderr)
        return 1

if __name__=="__main__":
    raise SystemExit(main())
