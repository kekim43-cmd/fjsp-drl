# Local Runbook

This fork keeps the original fjsp-drl API but applies compatibility fixes for a modern local Python stack.

## Smoke Test

On this machine, Python 3.13 already has CPU PyTorch installed. Install only the missing small runtime packages if needed:

```powershell
py -3.13 -m pip install --no-cache-dir "gym==0.26.2" pynvml
```

Run one pretrained inference case:

```powershell
$env:FJSP_NUM_INS='1'
$env:FJSP_NUM_AVERAGE='1'
py -3.13 test.py
```

Expected result from the first verified run:

```text
loading checkpoint: save_10_5.pt
rule: save_10_5.pt
Create env[0]
finish env 0
```

The generated makespan workbook contained:

```text
3128_10j_5m.fjs, save_10_5.pt, makespan 122
```

## Clean Environment

If there is enough disk space for PyTorch, prefer an isolated Python 3.10 environment:

```powershell
uv venv --python 3.10 .venv
.venv\Scripts\python.exe -m pip install -r requirements-local.txt
```

The original code targeted older Gym/Pandas/OpenPyXL behavior. Current patches keep the existing `reset()` and `step()` return contracts, so migration to Gymnasium should be treated as a separate implementation task.
