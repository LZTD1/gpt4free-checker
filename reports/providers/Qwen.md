# Qwen

- **Label:** Qwen
- **URL:** https://chat.qwen.ai
- **Models:** 19
- **Working tests:** 3 / 19
- **Avg response time:** 7.71s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `qwen3.5-max-2026-03-08` | text | ✅ `ok` | 8.46s | contains expected token 'PONG' |
| `qwen3.6-max-preview` | text | ✅ `ok` | 7.90s | contains expected token 'PONG' |
| `qwen3.6-plus-preview` | text | ✅ `ok` | 6.78s | contains expected token 'PONG' |
| `qwen-max-latest` | image | ❌ `exception` | 30.98s | NoMediaResponseError: No media response from Qwen |
| `qwen-plus-2025-07-28` | image | ❌ `exception` | 37.71s | NoMediaResponseError: No media response from Qwen |
| `qwen3-coder-plus` | image | ❌ `exception` | 40.78s | NoMediaResponseError: No media response from Qwen |
| `qwen3-max-2026-01-23` | image | ❌ `exception` | 26.73s | NoMediaResponseError: No media response from Qwen |
| `qwen3-omni-flash-2025-12-01` | image | ❌ `exception` | 30.75s | NoMediaResponseError: No media response from Qwen |
| `qwen3-vl-plus` | image | ❌ `timeout` | 93.69s | Timeout limit exceeded |
| `qwen3.5-122b-a10b` | image | ❌ `exception` | 36.72s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-27b` | image | ❌ `exception` | 31.46s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-35b-a3b` | image | ❌ `exception` | 29.02s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-397b-a17b` | image | ❌ `exception` | 35.02s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-flash` | image | ❌ `exception` | 27.24s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-omni-flash` | image | ❌ `exception` | 34.01s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-omni-plus` | image | ❌ `timeout` | 85.64s | Timeout limit exceeded |
| `qwen3.5-plus` | image | ❌ `exception` | 26.78s | NoMediaResponseError: No media response from Qwen |
| `qwen3.6-35b-a3b` | image | ❌ `exception` | 26.61s | NoMediaResponseError: No media response from Qwen |
| `qwen3.6-plus` | image | ❌ `exception` | 27.47s | NoMediaResponseError: No media response from Qwen |

## Sample successful responses

### `qwen3.5-max-2026-03-08` — text

```
PONG
```

### `qwen3.6-max-preview` — text

```
PONG
```

### `qwen3.6-plus-preview` — text

```
PONG
```

