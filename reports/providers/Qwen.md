# Qwen

- **Label:** Qwen
- **URL:** https://chat.qwen.ai
- **Models:** 19
- **Working tests:** 3 / 19
- **Avg response time:** 11.94s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `qwen3.5-max-2026-03-08` | text | ✅ `ok` | 14.14s | contains expected token 'PONG' |
| `qwen3.6-max-preview` | text | ✅ `ok` | 13.61s | contains expected token 'PONG' |
| `qwen3.6-plus-preview` | text | ✅ `ok` | 8.09s | contains expected token 'PONG' |
| `qwen-max-latest` | image | ❌ `http_error` | 28.74s | RuntimeError: Response: {'success': False, 'request_id': '7592d5af-5781-446e-8355-e2d270aa62c3', 'data': {'code': 'Not_Found', 'details': 'Model not found'}} |
| `qwen-plus-2025-07-28` | image | ❌ `timeout` | 36.00s | Timeout limit exceeded |
| `qwen3-coder-plus` | image | ❌ `exception` | 38.90s | NoMediaResponseError: No media response from Qwen |
| `qwen3-max-2026-01-23` | image | ❌ `exception` | 28.01s | NoMediaResponseError: No media response from Qwen |
| `qwen3-omni-flash-2025-12-01` | image | ❌ `exception` | 34.70s | NoMediaResponseError: No media response from Qwen |
| `qwen3-vl-plus` | image | ❌ `timeout` | 77.78s | Timeout limit exceeded |
| `qwen3.5-122b-a10b` | image | ❌ `exception` | 30.29s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-27b` | image | ❌ `exception` | 29.49s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-35b-a3b` | image | ❌ `exception` | 30.78s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-397b-a17b` | image | ❌ `timeout` | 37.51s | Timeout limit exceeded |
| `qwen3.5-flash` | image | ❌ `exception` | 31.23s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-omni-flash` | image | ❌ `timeout` | 47.89s | Timeout limit exceeded |
| `qwen3.5-omni-plus` | image | ❌ `timeout` | 40.47s | Timeout limit exceeded |
| `qwen3.5-plus` | image | ❌ `exception` | 33.38s | NoMediaResponseError: No media response from Qwen |
| `qwen3.6-35b-a3b` | image | ❌ `exception` | 32.89s | NoMediaResponseError: No media response from Qwen |
| `qwen3.6-plus` | image | ❌ `exception` | 43.00s | NoMediaResponseError: No media response from Qwen |

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

