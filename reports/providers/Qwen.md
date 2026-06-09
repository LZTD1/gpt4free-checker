# Qwen

- **Label:** Qwen
- **URL:** https://chat.qwen.ai
- **Models:** 19
- **Working tests:** 3 / 19
- **Avg response time:** 9.05s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `qwen3.5-max-2026-03-08` | text | ✅ `ok` | 11.85s | contains expected token 'PONG' |
| `qwen3.6-max-preview` | text | ✅ `ok` | 9.52s | contains expected token 'PONG' |
| `qwen3.6-plus-preview` | text | ✅ `ok` | 5.78s | contains expected token 'PONG' |
| `qwen-max-latest` | image | ❌ `http_error` | 19.72s | RuntimeError: Response: {'success': False, 'request_id': '54f6d7c5-3628-42b6-9d72-2520d35918e9', 'data': {'code': 'Not_Found', 'details': 'Model not found'}} |
| `qwen-plus-2025-07-28` | image | ❌ `exception` | 35.17s | NoMediaResponseError: No media response from Qwen |
| `qwen3-coder-plus` | image | ❌ `exception` | 32.04s | NoMediaResponseError: No media response from Qwen |
| `qwen3-max-2026-01-23` | image | ❌ `exception` | 25.69s | NoMediaResponseError: No media response from Qwen |
| `qwen3-omni-flash-2025-12-01` | image | ❌ `timeout` | 47.70s | Timeout limit exceeded |
| `qwen3-vl-plus` | image | ❌ `timeout` | 108.39s | Timeout limit exceeded |
| `qwen3.5-122b-a10b` | image | ❌ `exception` | 34.37s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-27b` | image | ❌ `exception` | 26.92s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-35b-a3b` | image | ❌ `exception` | 33.85s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-397b-a17b` | image | ❌ `timeout` | 50.46s | Timeout limit exceeded |
| `qwen3.5-flash` | image | ❌ `exception` | 30.45s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-omni-flash` | image | ❌ `timeout` | 40.22s | Timeout limit exceeded |
| `qwen3.5-omni-plus` | image | ❌ `timeout` | 35.36s | Timeout limit exceeded |
| `qwen3.5-plus` | image | ❌ `exception` | 28.25s | NoMediaResponseError: No media response from Qwen |
| `qwen3.6-35b-a3b` | image | ❌ `exception` | 22.60s | NoMediaResponseError: No media response from Qwen |
| `qwen3.6-plus` | image | ❌ `exception` | 33.65s | NoMediaResponseError: No media response from Qwen |

## Sample successful responses

### `qwen3.6-max-preview` — text

```
PONG
```

### `qwen3.5-max-2026-03-08` — text

```
PONG
```

### `qwen3.6-plus-preview` — text

```
PONG
```

