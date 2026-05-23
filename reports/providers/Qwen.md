# Qwen

- **Label:** Qwen
- **URL:** https://chat.qwen.ai
- **Models:** 19
- **Working tests:** 3 / 19
- **Avg response time:** 7.85s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `qwen3.5-max-2026-03-08` | text | ✅ `ok` | 10.50s | contains expected token 'PONG' |
| `qwen3.6-max-preview` | text | ✅ `ok` | 7.29s | contains expected token 'PONG' |
| `qwen3.6-plus-preview` | text | ✅ `ok` | 5.76s | contains expected token 'PONG' |
| `qwen-max-latest` | image | ❌ `exception` | 42.79s | NoMediaResponseError: No media response from Qwen |
| `qwen-plus-2025-07-28` | image | ❌ `exception` | 36.22s | NoMediaResponseError: No media response from Qwen |
| `qwen3-coder-plus` | image | ❌ `exception` | 42.48s | NoMediaResponseError: No media response from Qwen |
| `qwen3-max-2026-01-23` | image | ❌ `exception` | 31.58s | NoMediaResponseError: No media response from Qwen |
| `qwen3-omni-flash-2025-12-01` | image | ❌ `exception` | 32.73s | NoMediaResponseError: No media response from Qwen |
| `qwen3-vl-plus` | image | ❌ `timeout` | 58.50s | Timeout limit exceeded |
| `qwen3.5-122b-a10b` | image | ❌ `timeout` | 46.30s | Timeout limit exceeded |
| `qwen3.5-27b` | image | ❌ `exception` | 31.32s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-35b-a3b` | image | ❌ `exception` | 30.48s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-397b-a17b` | image | ❌ `exception` | 38.85s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-flash` | image | ❌ `exception` | 22.51s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-omni-flash` | image | ❌ `timeout` | 76.86s | Timeout limit exceeded |
| `qwen3.5-omni-plus` | image | ❌ `exception` | 41.51s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-plus` | image | ❌ `exception` | 36.06s | NoMediaResponseError: No media response from Qwen |
| `qwen3.6-35b-a3b` | image | ❌ `exception` | 34.74s | NoMediaResponseError: No media response from Qwen |
| `qwen3.6-plus` | image | ❌ `exception` | 33.81s | NoMediaResponseError: No media response from Qwen |

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

