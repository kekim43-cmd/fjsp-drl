# fjsp-drl Implementation Roadmap

## Current Baseline

- Upstream cloned: `songwenas12/fjsp-drl`, commit `d7637b7`.
- Pretrained model load verified: `model/save_10_5.pt`.
- One-instance inference verified on CPU with `FJSP_NUM_INS=1` and `FJSP_NUM_AVERAGE=1`.
- First verified output: `3128_10j_5m.fjs` solved with makespan `122`.

## Week 2 - Reproducible Execution

- Stabilize local execution with modern Python/Gym/Pandas/OpenPyXL.
- Keep a short smoke test command in `LOCAL_RUNBOOK.md`.
- Annotate real signatures in `env/fjsp_env.py`, `PPO_model.py`, and `graph/hgnn.py`.
- Replace guessed pseudocode in the week 2 walkthrough with actual class and method names.

## Week 3 - RTD Mapping Adapter

- Define an adapter from RTD state to fjsp-drl graph state.
- Expose policy output as `top_k[(operation, machine, score)]`.
- Split joint policy into What-Next and Where-Next views for rule-builder UI.

## Week 4 - Baseline Rule Simulation

- Implement simple PDR baselines: SPT, FIFO, earliest machine availability, priority first.
- Run the same FJSP instances through DRL and PDR baselines.
- Save makespan/time comparison tables for presentation and later API tests.

## Week 5 - Feature Schema Extension

- Add operation features for priority, due date, queue time, and product family.
- Add machine features for idle duration and availability window.
- Keep default behavior identical when these fields are absent.

## Week 6 - Reward Extension

- Introduce weighted reward terms for makespan, tardiness, setup continuity, and priority.
- Store weights in config instead of hard-coding.
- Add a small regression test proving the original makespan-only reward is unchanged when extension weights are zero.

## Week 7 - Dynamic Arrival Prototype

- Add optional job release times.
- Mask operations whose release time is greater than current environment time.
- Measure zero-shot policy degradation against static FJSP.

## Week 8 - Rule Builder Backend

- Convert policy candidates into rule-card payloads.
- Provide deterministic JSON output for frontend integration.
- Add a CLI command for one-shot recommendation from an instance file.

## Week 9 - Evaluation Package

- Batch-run public and synthetic test sets.
- Export makespan, runtime, feasibility flag, and selected action trace.
- Produce summary charts for DRL vs rule baselines.

## Week 10 - Packaging

- Add a stable module entry point for inference.
- Separate training-only dependencies from inference dependencies.
- Prepare Docker or conda instructions if disk/GPU resources are available.

## Week 11 - Demo Integration

- Connect the recommendation payload to the no-code RTD rule-builder demo.
- Show What-Next/Where-Next suggestions and simulated makespan delta.
- Keep manual rule override in the loop.

## Week 12-13 - Finalization

- Freeze reproducible commands, limitations, and benchmark numbers.
- Update slides and report with verified code results, not assumptions.
- Mark Gymnasium migration, large-scale retraining, batch tools, and cluster tools as future work unless implementation time remains.
