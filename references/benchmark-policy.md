# Benchmark policy

Keep four evidence classes separate:

1. published external benchmark results;
2. local behavioral evaluations actually run;
3. deterministic script/unit tests;
4. engineering heuristics.

A leaderboard compilation is not a benchmark rerun.

## Comparable observation key

Preserve model, effort, environment/surface, dataset version, protocol/harness, tool configuration, evaluator, metric, and evidence status. Unknown metadata does not become “same configuration”.

Use `scripts/aggregate_benchmarks.py data.json --output results.json`. The example file is schema-only and synthetic.

Duplicate copies of the same experiment must not count as independent runs. Without run-level data, do not invent confidence intervals. Do not mix percentages, Elo, cost, and composite indices into one average.

A domain macro mean is descriptive only when every predeclared component has comparable coverage. Missing components produce null/insufficient coverage rather than zero.

## Local calibration

Freeze task, inputs, tools, rubric, and gates before a run. Keep evaluator criteria separate from the worker where possible. Use fresh contexts, save raw outputs, distinguish development from holdout, and preserve model/effort identity from actual runtime controls rather than prompting the model to claim an identity.

All-pass can mean a ceiling; all-fail can mean a floor or bad setup. Neither proves configurations are equal.

Routing policies should be promoted only when they preserve critical acceptance gates on relevant tasks and holdout evidence.
