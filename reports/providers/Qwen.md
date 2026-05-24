# Qwen

- **Label:** Qwen
- **URL:** https://chat.qwen.ai
- **Models:** 19
- **Working tests:** 3 / 19
- **Avg response time:** 8.46s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `qwen3.5-max-2026-03-08` | text | ✅ `ok` | 10.14s | contains expected token 'PONG' |
| `qwen3.6-max-preview` | text | ✅ `ok` | 9.83s | contains expected token 'PONG' |
| `qwen3.6-plus-preview` | text | ✅ `ok` | 5.40s | contains expected token 'PONG' |
| `qwen-max-latest` | image | ❌ `timeout` | 206.91s | Timeout limit exceeded |
| `qwen-plus-2025-07-28` | image | ❌ `exception` | 42.34s | NoMediaResponseError: No media response from Qwen |
| `qwen3-coder-plus` | image | ❌ `timeout` | 59.09s | Timeout limit exceeded |
| `qwen3-max-2026-01-23` | image | ❌ `exception` | 40.89s | NoMediaResponseError: No media response from Qwen |
| `qwen3-omni-flash-2025-12-01` | image | ❌ `exception` | 36.32s | NoMediaResponseError: No media response from Qwen |
| `qwen3-vl-plus` | image | ❌ `timeout` | 59.79s | Timeout limit exceeded |
| `qwen3.5-122b-a10b` | image | ❌ `exception` | 11.65s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-27b` | image | ❌ `exception` | 33.73s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-35b-a3b` | image | ❌ `exception` | 37.65s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-397b-a17b` | image | ❌ `timeout` | 44.70s | Timeout limit exceeded |
| `qwen3.5-flash` | image | ❌ `exception` | 29.74s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-omni-flash` | image | ❌ `timeout` | 3511.69s | Timeout limit exceeded |
| `qwen3.5-omni-plus` | image | ❌ `exception` | 33.43s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-plus` | image | ❌ `exception` | 35.98s | NoMediaResponseError: No media response from Qwen |
| `qwen3.6-35b-a3b` | image | ❌ `timeout` | 30.44s | Timeout limit exceeded |
| `qwen3.6-plus` | image | ❌ `exception` | 36.14s | NoMediaResponseError: No media response from Qwen |

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

