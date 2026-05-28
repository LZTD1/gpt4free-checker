# Qwen

- **Label:** Qwen
- **URL:** https://chat.qwen.ai
- **Models:** 19
- **Working tests:** 3 / 19
- **Avg response time:** 13.56s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `qwen3.5-max-2026-03-08` | text | ✅ `ok` | 7.86s | contains expected token 'PONG' |
| `qwen3.6-max-preview` | text | ✅ `ok` | 23.93s | contains expected token 'PONG' |
| `qwen3.6-plus-preview` | text | ✅ `ok` | 8.89s | contains expected token 'PONG' |
| `qwen-max-latest` | image | ❌ `exception` | 38.85s | NoMediaResponseError: No media response from Qwen |
| `qwen-plus-2025-07-28` | image | ❌ `exception` | 41.74s | NoMediaResponseError: No media response from Qwen |
| `qwen3-coder-plus` | image | ❌ `exception` | 34.16s | NoMediaResponseError: No media response from Qwen |
| `qwen3-max-2026-01-23` | image | ❌ `exception` | 34.27s | NoMediaResponseError: No media response from Qwen |
| `qwen3-omni-flash-2025-12-01` | image | ❌ `exception` | 22.77s | NoMediaResponseError: No media response from Qwen |
| `qwen3-vl-plus` | image | ❌ `timeout` | 43.98s | Timeout limit exceeded |
| `qwen3.5-122b-a10b` | image | ❌ `exception` | 32.01s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-27b` | image | ❌ `exception` | 38.91s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-35b-a3b` | image | ❌ `exception` | 34.65s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-397b-a17b` | image | ❌ `timeout` | 41.57s | Timeout limit exceeded |
| `qwen3.5-flash` | image | ❌ `exception` | 32.72s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-omni-flash` | image | ❌ `exception` | 32.11s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-omni-plus` | image | ❌ `exception` | 44.96s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-plus` | image | ❌ `exception` | 37.84s | NoMediaResponseError: No media response from Qwen |
| `qwen3.6-35b-a3b` | image | ❌ `exception` | 38.70s | NoMediaResponseError: No media response from Qwen |
| `qwen3.6-plus` | image | ❌ `exception` | 39.00s | NoMediaResponseError: No media response from Qwen |

## Sample successful responses

### `qwen3.5-max-2026-03-08` — text

```
PONG
```

### `qwen3.6-plus-preview` — text

```
PONG
```

### `qwen3.6-max-preview` — text

```
PONG
```

