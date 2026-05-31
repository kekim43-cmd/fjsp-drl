# Execution Proof

## Purpose

This run is a short CPU-only training run for submission evidence. It proves that the fjsp-drl source code executes the training loop, performs validation, writes model checkpoints, and exports result workbooks. It is not intended to reproduce fully converged paper-level training.

## Environment

- Date: 2026-05-31
- Python: `py -3.13`
- PyTorch: `2.10.0+cpu`
- CUDA/GPU: unavailable on this local machine
- Training mode: reduced CPU smoke training

## Commands Run

Syntax check:

```powershell
py -3.13 -m py_compile train.py test.py validate.py env\fjsp_env.py
```

Short training:

```powershell
cmd /c "set FJSP_MAX_ITERATIONS=10&& set FJSP_SAVE_TIMESTEP=5&& set FJSP_VALID_BATCH_SIZE=10&& set FJSP_BATCH_SIZE=4&& set FJSP_VIZ=false&& py -3.13 train.py > train_output_clean.log 2>&1"
```

Pretrained inference smoke test:

```powershell
cmd /c "set FJSP_NUM_INS=1&& set FJSP_NUM_AVERAGE=1&& py -3.13 test.py > test_output_clean.log 2>&1"
```

## Training Evidence

Log file:

- `train_output_clean.log`

Key log lines:

```text
PyTorch device:  cpu
reward:  -62.650 ; loss:  0.348
Start validating
There are 10 dev instances.
validating time:  0.5020437240600586
Start validating
There are 10 dev instances.
validating time:  0.579848051071167
total_time:  9.812803745269775
```

Generated training artifacts:

- `save/train_20260531_200020/save_best_10_5_5.pt`
- `save/train_20260531_200020/training_ave_20260531_200020.xlsx`
- `save/train_20260531_200020/training_100_20260531_200020.xlsx`

Verified workbook values:

```text
training_ave rows: 3, cols: 2
headers: iterations, res
row 2: 5, 111.1999969482422
row 3: 10, 114.3000030517578
```

## Inference Evidence

Log file:

- `test_output_clean.log`

Generated inference artifacts:

- `save/test_20260531_200041/makespan_20260531_200041.xlsx`
- `save/test_20260531_200041/time_20260531_200041.xlsx`

Verified inference workbook value:

```text
file_name: 3128_10j_5m.fjs
checkpoint: save_10_5.pt
makespan: 122
```

## Notes

- Gym prints a maintenance warning because the upstream project uses legacy `gym`. The warning does not stop execution.
- This repository includes compatibility patches for modern Gym, pandas/openpyxl, CPU-only execution, and short-run environment variable overrides.
