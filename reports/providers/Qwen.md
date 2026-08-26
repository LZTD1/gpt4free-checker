# Qwen

- **Label:** Qwen
- **URL:** https://chat.qwen.ai
- **Models:** 23
- **Working tests:** 1 / 23
- **Avg response time:** 22.34s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `qwen3.6-max-preview` | text | ✅ `ok` | 22.34s | contains expected token 'PONG' |
| `qwen-latest-series-invite-beta-v16` | text | ❌ `http_error` | 0.93s | RuntimeError: Response: {'success': False, 'request_id': '1ace2a16-587c-45cf-b540-f29f2bddb82f', 'data': {'code': 'Not_Found', 'details': 'Model not found'}} |
| `qwen-latest-series-invite-beta-v24` | text | ❌ `http_error` | 0.65s | RuntimeError: Response: {'success': False, 'request_id': '7cd8a32b-55fa-40bd-9a3d-5ab8258c66ad', 'data': {'code': 'Not_Found', 'details': 'Model not found'}} |
| `qwen-plus-2025-07-28` | image | ❌ `exception` | 41.29s | NoMediaResponseError: No media response from Qwen |
| `qwen3-coder-plus` | image | ❌ `exception` | 41.25s | NoMediaResponseError: No media response from Qwen |
| `qwen3-max-2026-01-23` | image | ❌ `exception` | 41.24s | NoMediaResponseError: No media response from Qwen |
| `qwen3-omni-flash-2025-12-01` | image | ❌ `exception` | 41.47s | NoMediaResponseError: No media response from Qwen |
| `qwen3-vl-plus` | image | ❌ `exception` | 41.28s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-122b-a10b` | image | ❌ `http_error` | 0.74s | RuntimeError: Response: {'success': False, 'request_id': '9f24824d-de18-4a56-88f4-7e4eb7f1a900', 'data': {'code': 'Not_Found', 'details': 'Model not found'}} |
| `qwen3.5-27b` | image | ❌ `http_error` | 0.69s | RuntimeError: Response: {'success': False, 'request_id': '78971630-f729-4a2c-b482-6aaae87abc94', 'data': {'code': 'Not_Found', 'details': 'Model not found'}} |
| `qwen3.5-35b-a3b` | image | ❌ `http_error` | 0.88s | RuntimeError: Response: {'success': False, 'request_id': 'e4ab7dd8-7109-469a-a0e5-2c9a4be1441f', 'data': {'code': 'Not_Found', 'details': 'Model not found'}} |
| `qwen3.5-397b-a17b` | image | ❌ `exception` | 41.45s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-flash` | image | ❌ `exception` | 21.02s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-max-2026-03-08` | text | ❌ `http_error` | 0.70s | RuntimeError: Response: {'success': False, 'request_id': 'd91e849f-8e16-4ff2-af7c-454f57fd21ed', 'data': {'code': 'Not_Found', 'details': 'Model not found'}} |
| `qwen3.5-omni-flash` | image | ❌ `exception` | 43.05s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-omni-plus` | image | ❌ `exception` | 21.03s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-plus` | image | ❌ `exception` | 22.02s | ResponseError: quota_limit: The service is currently experiencing high demand. Please try again later. |
| `qwen3.6-27b` | image | ❌ `exception` | 21.02s | NoMediaResponseError: No media response from Qwen |
| `qwen3.6-35b-a3b` | image | ❌ `exception` | 22.02s | NoMediaResponseError: No media response from Qwen |
| `qwen3.6-plus` | image | ❌ `exception` | 21.02s | ResponseError: internal_error: An unexpected error occurred. Please try again later, or report the issue by emailing DPO_qwenlm-intl@service.alibaba.com. |
| `qwen3.6-plus-preview` | text | ❌ `http_error` | 0.66s | RuntimeError: Response: {'success': False, 'request_id': 'd1112fd4-371e-4352-b477-b93455792d4b', 'data': {'code': 'Not_Found', 'details': 'Model not found'}} |
| `qwen3.7-max` | image | ❌ `exception` | 21.03s | ResponseError: internal_error: An unexpected error occurred. Please try again later, or report the issue by emailing DPO_qwenlm-intl@service.alibaba.com. |
| `qwen3.7-plus` | image | ❌ `exception` | 22.02s | ResponseError: internal_error: An unexpected error occurred. Please try again later, or report the issue by emailing DPO_qwenlm-intl@service.alibaba.com. |

## Sample successful responses

### `qwen3.6-max-preview` — text

```
PONG
```

