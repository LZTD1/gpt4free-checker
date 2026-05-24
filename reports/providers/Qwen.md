# Qwen

- **Label:** Qwen
- **URL:** https://chat.qwen.ai
- **Models:** 19
- **Working tests:** 3 / 19
- **Avg response time:** 7.23s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `qwen3.5-max-2026-03-08` | text | ✅ `ok` | 8.57s | contains expected token 'PONG' |
| `qwen3.6-max-preview` | text | ✅ `ok` | 6.52s | contains expected token 'PONG' |
| `qwen3.6-plus-preview` | text | ✅ `ok` | 6.60s | contains expected token 'PONG' |
| `qwen-max-latest` | image | ❌ `exception` | 34.65s | NoMediaResponseError: No media response from Qwen |
| `qwen-plus-2025-07-28` | image | ❌ `exception` | 43.50s | NoMediaResponseError: No media response from Qwen |
| `qwen3-coder-plus` | image | ❌ `exception` | 44.27s | NoMediaResponseError: No media response from Qwen |
| `qwen3-max-2026-01-23` | image | ❌ `exception` | 30.65s | NoMediaResponseError: No media response from Qwen |
| `qwen3-omni-flash-2025-12-01` | image | ❌ `timeout` | 69.81s | Timeout limit exceeded |
| `qwen3-vl-plus` | image | ❌ `timeout` | 58.32s | Timeout limit exceeded |
| `qwen3.5-122b-a10b` | image | ❌ `exception` | 37.03s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-27b` | image | ❌ `exception` | 27.32s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-35b-a3b` | image | ❌ `exception` | 32.84s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-397b-a17b` | image | ❌ `timeout` | 70.36s | Timeout limit exceeded |
| `qwen3.5-flash` | image | ❌ `exception` | 28.98s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-omni-flash` | image | ❌ `exception` | 38.59s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-omni-plus` | image | ❌ `timeout` | 57.05s | Timeout limit exceeded |
| `qwen3.5-plus` | image | ❌ `exception` | 32.97s | NoMediaResponseError: No media response from Qwen |
| `qwen3.6-35b-a3b` | image | ❌ `exception` | 35.08s | NoMediaResponseError: No media response from Qwen |
| `qwen3.6-plus` | image | ❌ `exception` | 35.66s | NoMediaResponseError: No media response from Qwen |

## Sample successful responses

### `qwen3.6-plus-preview` — text

```
PONG
```

### `qwen3.6-max-preview` — text

```
PONG
```

### `qwen3.5-max-2026-03-08` — text

```
PONG
```

