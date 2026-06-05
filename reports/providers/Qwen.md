# Qwen

- **Label:** Qwen
- **URL:** https://chat.qwen.ai
- **Models:** 19
- **Working tests:** 3 / 19
- **Avg response time:** 9.19s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `qwen3.5-max-2026-03-08` | text | ✅ `ok` | 10.17s | contains expected token 'PONG' |
| `qwen3.6-max-preview` | text | ✅ `ok` | 7.09s | contains expected token 'PONG' |
| `qwen3.6-plus-preview` | text | ✅ `ok` | 10.31s | contains expected token 'PONG' |
| `qwen-max-latest` | image | ❌ `http_error` | 20.79s | RuntimeError: Response: {'success': False, 'request_id': 'a96cfa3c-9091-46f4-a89d-5cf3c89d53e1', 'data': {'code': 'Not_Found', 'details': 'Model not found'}} |
| `qwen-plus-2025-07-28` | image | ❌ `exception` | 33.00s | NoMediaResponseError: No media response from Qwen |
| `qwen3-coder-plus` | image | ❌ `exception` | 38.16s | NoMediaResponseError: No media response from Qwen |
| `qwen3-max-2026-01-23` | image | ❌ `exception` | 31.05s | NoMediaResponseError: No media response from Qwen |
| `qwen3-omni-flash-2025-12-01` | image | ❌ `timeout` | 44.05s | Timeout limit exceeded |
| `qwen3-vl-plus` | image | ❌ `timeout` | 97.79s | Timeout limit exceeded |
| `qwen3.5-122b-a10b` | image | ❌ `exception` | 29.11s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-27b` | image | ❌ `exception` | 28.23s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-35b-a3b` | image | ❌ `exception` | 22.35s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-397b-a17b` | image | ❌ `timeout` | 46.50s | Timeout limit exceeded |
| `qwen3.5-flash` | image | ❌ `exception` | 25.90s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-omni-flash` | image | ❌ `exception` | 34.45s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-omni-plus` | image | ❌ `exception` | 28.19s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-plus` | image | ❌ `exception` | 28.33s | NoMediaResponseError: No media response from Qwen |
| `qwen3.6-35b-a3b` | image | ❌ `timeout` | 76.12s | Timeout limit exceeded |
| `qwen3.6-plus` | image | ❌ `exception` | 31.47s | NoMediaResponseError: No media response from Qwen |

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

