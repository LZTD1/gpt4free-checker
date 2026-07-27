# Qwen

- **Label:** Qwen
- **URL:** https://chat.qwen.ai
- **Models:** 23
- **Working tests:** 1 / 23
- **Avg response time:** 22.12s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `qwen3.6-max-preview` | text | ✅ `ok` | 22.12s | contains expected token 'PONG' |
| `qwen-latest-series-invite-beta-v16` | text | ❌ `rate_limited` | 1.08s | RuntimeError: Response: {'success': False, 'request_id': '606848c6-d6aa-42ff-a429-05319c545541', 'data': {'code': 'Not_Found', 'details': 'Model not found'}} |
| `qwen-latest-series-invite-beta-v24` | text | ❌ `http_error` | 0.96s | RuntimeError: Response: {'success': False, 'request_id': '8a0a9eb5-3d68-49f1-a2a2-306035428ba4', 'data': {'code': 'Not_Found', 'details': 'Model not found'}} |
| `qwen-plus-2025-07-28` | image | ❌ `exception` | 21.03s | NoMediaResponseError: No media response from Qwen |
| `qwen3-coder-plus` | image | ❌ `exception` | 21.03s | NoMediaResponseError: No media response from Qwen |
| `qwen3-max-2026-01-23` | image | ❌ `exception` | 21.03s | NoMediaResponseError: No media response from Qwen |
| `qwen3-omni-flash-2025-12-01` | image | ❌ `exception` | 41.35s | NoMediaResponseError: No media response from Qwen |
| `qwen3-vl-plus` | image | ❌ `exception` | 22.03s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-122b-a10b` | image | ❌ `http_error` | 0.96s | RuntimeError: Response: {'success': False, 'request_id': '0b99be78-9bde-425f-9c04-e3b9c719bdf0', 'data': {'code': 'Not_Found', 'details': 'Model not found'}} |
| `qwen3.5-27b` | image | ❌ `http_error` | 0.91s | RuntimeError: Response: {'success': False, 'request_id': '95b4bffd-be17-4e41-90a7-d16df1e66f19', 'data': {'code': 'Not_Found', 'details': 'Model not found'}} |
| `qwen3.5-35b-a3b` | image | ❌ `http_error` | 1.03s | RuntimeError: Response: {'success': False, 'request_id': 'e3ed709c-1e0b-4880-876e-25cc41485663', 'data': {'code': 'Not_Found', 'details': 'Model not found'}} |
| `qwen3.5-397b-a17b` | image | ❌ `exception` | 41.07s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-flash` | image | ❌ `exception` | 21.03s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-max-2026-03-08` | text | ❌ `http_error` | 0.96s | RuntimeError: Response: {'success': False, 'request_id': '14c2720c-a42c-451d-a133-d2f450851e6f', 'data': {'code': 'Not_Found', 'details': 'Model not found'}} |
| `qwen3.5-omni-flash` | image | ❌ `timeout` | 45.49s | Timeout limit exceeded |
| `qwen3.5-omni-plus` | image | ❌ `exception` | 21.03s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-plus` | image | ❌ `exception` | 41.46s | NoMediaResponseError: No media response from Qwen |
| `qwen3.6-27b` | image | ❌ `exception` | 41.15s | NoMediaResponseError: No media response from Qwen |
| `qwen3.6-35b-a3b` | image | ❌ `exception` | 22.02s | NoMediaResponseError: No media response from Qwen |
| `qwen3.6-plus` | image | ❌ `exception` | 41.44s | NoMediaResponseError: No media response from Qwen |
| `qwen3.6-plus-preview` | text | ❌ `http_error` | 0.89s | RuntimeError: Response: {'success': False, 'request_id': 'b310c7f3-92a9-45ee-b0f8-55d953d9995e', 'data': {'code': 'Not_Found', 'details': 'Model not found'}} |
| `qwen3.7-max` | image | ❌ `exception` | 21.03s | NoMediaResponseError: No media response from Qwen |
| `qwen3.7-plus` | image | ❌ `exception` | 22.03s | NoMediaResponseError: No media response from Qwen |

## Sample successful responses

### `qwen3.6-max-preview` — text

```
PONG
```

