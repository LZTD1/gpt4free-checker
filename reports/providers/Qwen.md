# Qwen

- **Label:** Qwen
- **URL:** https://chat.qwen.ai
- **Models:** 19
- **Working tests:** 3 / 19
- **Avg response time:** 8.40s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `qwen3.5-max-2026-03-08` | text | ✅ `ok` | 9.70s | contains expected token 'PONG' |
| `qwen3.6-max-preview` | text | ✅ `ok` | 9.24s | contains expected token 'PONG' |
| `qwen3.6-plus-preview` | text | ✅ `ok` | 6.28s | contains expected token 'PONG' |
| `qwen-max-latest` | image | ❌ `http_error` | 27.64s | RuntimeError: Response: {'success': False, 'request_id': '723aa8ff-26e2-4eef-8375-03bfc8d8dcaa', 'data': {'code': 'Not_Found', 'details': 'Model not found'}} |
| `qwen-plus-2025-07-28` | image | ❌ `timeout` | 44.97s | Timeout limit exceeded |
| `qwen3-coder-plus` | image | ❌ `exception` | 28.22s | NoMediaResponseError: No media response from Qwen |
| `qwen3-max-2026-01-23` | image | ❌ `exception` | 31.98s | NoMediaResponseError: No media response from Qwen |
| `qwen3-omni-flash-2025-12-01` | image | ❌ `exception` | 33.09s | NoMediaResponseError: No media response from Qwen |
| `qwen3-vl-plus` | image | ❌ `timeout` | 53.36s | Timeout limit exceeded |
| `qwen3.5-122b-a10b` | image | ❌ `exception` | 29.30s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-27b` | image | ❌ `exception` | 34.78s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-35b-a3b` | image | ❌ `exception` | 28.73s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-397b-a17b` | image | ❌ `timeout` | 31.78s | Timeout limit exceeded |
| `qwen3.5-flash` | image | ❌ `exception` | 27.03s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-omni-flash` | image | ❌ `exception` | 40.50s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-omni-plus` | image | ❌ `exception` | 16.27s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-plus` | image | ❌ `exception` | 39.77s | NoMediaResponseError: No media response from Qwen |
| `qwen3.6-35b-a3b` | image | ❌ `exception` | 35.28s | NoMediaResponseError: No media response from Qwen |
| `qwen3.6-plus` | image | ❌ `exception` | 29.06s | NoMediaResponseError: No media response from Qwen |

## Sample successful responses

### `qwen3.6-plus-preview` — text

```
PONG
```

### `qwen3.5-max-2026-03-08` — text

```
PONG
```

### `qwen3.6-max-preview` — text

```
PONG
```

