# Qwen

- **Label:** Qwen
- **URL:** https://chat.qwen.ai
- **Models:** 23
- **Working tests:** 1 / 23
- **Avg response time:** 21.02s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `qwen3.6-max-preview` | text | ✅ `ok` | 21.02s | contains expected token 'PONG' |
| `qwen-latest-series-invite-beta-v16` | text | ❌ `http_error` | 0.74s | RuntimeError: Response: {'success': False, 'request_id': '71958140-cfca-4411-bf00-57d9fdc1ca01', 'data': {'code': 'Not_Found', 'details': 'Model not found'}} |
| `qwen-latest-series-invite-beta-v24` | text | ❌ `http_error` | 0.65s | RuntimeError: Response: {'success': False, 'request_id': 'a23e5781-c337-4801-8278-66b0789147b7', 'data': {'code': 'Not_Found', 'details': 'Model not found'}} |
| `qwen-plus-2025-07-28` | image | ❌ `exception` | 22.02s | NoMediaResponseError: No media response from Qwen |
| `qwen3-coder-plus` | image | ❌ `exception` | 41.09s | NoMediaResponseError: No media response from Qwen |
| `qwen3-max-2026-01-23` | image | ❌ `exception` | 20.46s | ResponseError: internal_error: Internal Error |
| `qwen3-omni-flash-2025-12-01` | image | ❌ `timeout` | 63.30s | Timeout limit exceeded |
| `qwen3-vl-plus` | image | ❌ `exception` | 22.02s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-122b-a10b` | image | ❌ `http_error` | 0.65s | RuntimeError: Response: {'success': False, 'request_id': 'f056a487-5e4d-4879-bd1a-048455a5d083', 'data': {'code': 'Not_Found', 'details': 'Model not found'}} |
| `qwen3.5-27b` | image | ❌ `http_error` | 0.61s | RuntimeError: Response: {'success': False, 'request_id': '6ef36cb0-55fb-4bed-8c5a-f7019ae86fca', 'data': {'code': 'Not_Found', 'details': 'Model not found'}} |
| `qwen3.5-35b-a3b` | image | ❌ `http_error` | 0.74s | RuntimeError: Response: {'success': False, 'request_id': 'b5a25bc4-4b0f-4358-a2de-be7186df29f3', 'data': {'code': 'Not_Found', 'details': 'Model not found'}} |
| `qwen3.5-397b-a17b` | image | ❌ `exception` | 21.02s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-flash` | image | ❌ `exception` | 41.06s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-max-2026-03-08` | text | ❌ `http_error` | 0.67s | RuntimeError: Response: {'success': False, 'request_id': '63783bb7-b6c0-4b44-a6c3-91fd317a266a', 'data': {'code': 'Not_Found', 'details': 'Model not found'}} |
| `qwen3.5-omni-flash` | image | ❌ `timeout` | 63.44s | Timeout limit exceeded |
| `qwen3.5-omni-plus` | image | ❌ `exception` | 21.02s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-plus` | image | ❌ `exception` | 22.01s | NoMediaResponseError: No media response from Qwen |
| `qwen3.6-27b` | image | ❌ `exception` | 23.53s | NoMediaResponseError: No media response from Qwen |
| `qwen3.6-35b-a3b` | image | ❌ `exception` | 8.21s | NoMediaResponseError: No media response from Qwen |
| `qwen3.6-plus` | image | ❌ `exception` | 22.02s | NoMediaResponseError: No media response from Qwen |
| `qwen3.6-plus-preview` | text | ❌ `http_error` | 0.64s | RuntimeError: Response: {'success': False, 'request_id': '29524b45-13dc-42be-9fee-5df2080f9cdb', 'data': {'code': 'Not_Found', 'details': 'Model not found'}} |
| `qwen3.7-max` | image | ❌ `exception` | 20.45s | NoMediaResponseError: No media response from Qwen |
| `qwen3.7-plus` | image | ❌ `exception` | 21.02s | NoMediaResponseError: No media response from Qwen |

## Sample successful responses

### `qwen3.6-max-preview` — text

```
PONG
```

