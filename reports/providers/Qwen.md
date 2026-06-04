# Qwen

- **Label:** Qwen
- **URL:** https://chat.qwen.ai
- **Models:** 19
- **Working tests:** 3 / 19
- **Avg response time:** 7.36s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `qwen3.5-max-2026-03-08` | text | ✅ `ok` | 10.72s | contains expected token 'PONG' |
| `qwen3.6-max-preview` | text | ✅ `ok` | 5.69s | contains expected token 'PONG' |
| `qwen3.6-plus-preview` | text | ✅ `ok` | 5.66s | contains expected token 'PONG' |
| `qwen-max-latest` | image | ❌ `http_error` | 25.09s | RuntimeError: Response: {'success': False, 'request_id': 'c893eab1-127e-4714-ad45-c3f136d6acd1', 'data': {'code': 'Not_Found', 'details': 'Model not found'}} |
| `qwen-plus-2025-07-28` | image | ❌ `exception` | 33.01s | NoMediaResponseError: No media response from Qwen |
| `qwen3-coder-plus` | image | ❌ `exception` | 34.84s | NoMediaResponseError: No media response from Qwen |
| `qwen3-max-2026-01-23` | image | ❌ `exception` | 23.25s | NoMediaResponseError: No media response from Qwen |
| `qwen3-omni-flash-2025-12-01` | image | ❌ `exception` | 19.63s | NoMediaResponseError: No media response from Qwen |
| `qwen3-vl-plus` | image | ❌ `timeout` | 32.76s | Timeout limit exceeded |
| `qwen3.5-122b-a10b` | image | ❌ `exception` | 30.98s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-27b` | image | ❌ `exception` | 26.89s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-35b-a3b` | image | ❌ `exception` | 26.61s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-397b-a17b` | image | ❌ `timeout` | 55.56s | Timeout limit exceeded |
| `qwen3.5-flash` | image | ❌ `exception` | 18.37s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-omni-flash` | image | ❌ `exception` | 34.26s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-omni-plus` | image | ❌ `exception` | 33.68s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-plus` | image | ❌ `exception` | 27.09s | NoMediaResponseError: No media response from Qwen |
| `qwen3.6-35b-a3b` | image | ❌ `exception` | 31.58s | NoMediaResponseError: No media response from Qwen |
| `qwen3.6-plus` | image | ❌ `exception` | 26.72s | NoMediaResponseError: No media response from Qwen |

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

