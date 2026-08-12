# Qwen

- **Label:** Qwen
- **URL:** https://chat.qwen.ai
- **Models:** 23
- **Working tests:** 1 / 23
- **Avg response time:** 22.22s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `qwen3.6-max-preview` | text | ✅ `ok` | 22.22s | contains expected token 'PONG' |
| `qwen-latest-series-invite-beta-v16` | text | ❌ `http_error` | 0.66s | RuntimeError: Response: {'success': False, 'request_id': '1bd0356f-ef78-44d1-9fe0-0e1e36d77a74', 'data': {'code': 'Not_Found', 'details': 'Model not found'}} |
| `qwen-latest-series-invite-beta-v24` | text | ❌ `http_error` | 0.71s | RuntimeError: Response: {'success': False, 'request_id': '81e293aa-0ef0-4917-857d-50ce4220ea1f', 'data': {'code': 'Not_Found', 'details': 'Model not found'}} |
| `qwen-plus-2025-07-28` | image | ❌ `exception` | 21.03s | NoMediaResponseError: No media response from Qwen |
| `qwen3-coder-plus` | image | ❌ `exception` | 20.68s | ResponseError: internal_error: Internal Error |
| `qwen3-max-2026-01-23` | image | ❌ `exception` | 21.03s | NoMediaResponseError: No media response from Qwen |
| `qwen3-omni-flash-2025-12-01` | image | ❌ `exception` | 22.03s | NoMediaResponseError: No media response from Qwen |
| `qwen3-vl-plus` | image | ❌ `exception` | 21.61s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-122b-a10b` | image | ❌ `http_error` | 0.70s | RuntimeError: Response: {'success': False, 'request_id': '754b8456-f9cf-471d-a277-4b686f95e0b3', 'data': {'code': 'Not_Found', 'details': 'Model not found'}} |
| `qwen3.5-27b` | image | ❌ `http_error` | 0.92s | RuntimeError: Response: {'success': False, 'request_id': 'fe4aa175-4a30-4533-a83c-f0d7dbffe0fc', 'data': {'code': 'Not_Found', 'details': 'Model not found'}} |
| `qwen3.5-35b-a3b` | image | ❌ `http_error` | 0.61s | RuntimeError: Response: {'success': False, 'request_id': '98ca2d76-2277-46a9-a486-a0b52969983b', 'data': {'code': 'Not_Found', 'details': 'Model not found'}} |
| `qwen3.5-397b-a17b` | image | ❌ `exception` | 21.03s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-flash` | image | ❌ `exception` | 41.22s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-max-2026-03-08` | text | ❌ `http_error` | 0.62s | RuntimeError: Response: {'success': False, 'request_id': 'd7d59b9d-cad4-4438-a66f-bbba8f5dc19d', 'data': {'code': 'Not_Found', 'details': 'Model not found'}} |
| `qwen3.5-omni-flash` | image | ❌ `timeout` | 63.49s | Timeout limit exceeded |
| `qwen3.5-omni-plus` | image | ❌ `exception` | 21.02s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-plus` | image | ❌ `exception` | 22.02s | NoMediaResponseError: No media response from Qwen |
| `qwen3.6-27b` | image | ❌ `exception` | 41.23s | NoMediaResponseError: No media response from Qwen |
| `qwen3.6-35b-a3b` | image | ❌ `exception` | 22.02s | NoMediaResponseError: No media response from Qwen |
| `qwen3.6-plus` | image | ❌ `exception` | 41.43s | NoMediaResponseError: No media response from Qwen |
| `qwen3.6-plus-preview` | text | ❌ `http_error` | 0.84s | RuntimeError: Response: {'success': False, 'request_id': '41647509-9bb9-4167-9d84-82ed463c2f80', 'data': {'code': 'Not_Found', 'details': 'Model not found'}} |
| `qwen3.7-max` | image | ❌ `exception` | 21.02s | NoMediaResponseError: No media response from Qwen |
| `qwen3.7-plus` | image | ❌ `exception` | 22.03s | NoMediaResponseError: No media response from Qwen |

## Sample successful responses

### `qwen3.6-max-preview` — text

```
PONG
```

