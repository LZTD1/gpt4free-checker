# Qwen

- **Label:** Qwen
- **URL:** https://chat.qwen.ai
- **Models:** 23
- **Working tests:** 1 / 23
- **Avg response time:** 41.90s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `qwen3.6-max-preview` | text | ✅ `ok` | 41.90s | contains expected token 'PONG' |
| `qwen-latest-series-invite-beta-v16` | text | ❌ `rate_limited` | 21.02s | RuntimeError: Response: {'success': False, 'request_id': 'c1e8c429-78a3-4eb7-bca8-e6256fd66985', 'data': {'code': 'Not_Found', 'details': 'Model not found'}} |
| `qwen-latest-series-invite-beta-v24` | text | ❌ `http_error` | 0.84s | RuntimeError: Response: {'success': False, 'request_id': 'e74ca4a0-ae3c-48c5-922b-13be9fa56ac7', 'data': {'code': 'Not_Found', 'details': 'Model not found'}} |
| `qwen-plus-2025-07-28` | image | ❌ `exception` | 21.02s | NoMediaResponseError: No media response from Qwen |
| `qwen3-coder-plus` | image | ❌ `exception` | 41.33s | NoMediaResponseError: No media response from Qwen |
| `qwen3-max-2026-01-23` | image | ❌ `exception` | 41.53s | NoMediaResponseError: No media response from Qwen |
| `qwen3-omni-flash-2025-12-01` | image | ❌ `exception` | 22.03s | NoMediaResponseError: No media response from Qwen |
| `qwen3-vl-plus` | image | ❌ `exception` | 0.98s | RuntimeError: Response: {'ret': ['FAIL_SYS_USER_VALIDATE', 'RGV587_ERROR::SM::哎哟喂,被挤爆啦,请稍后重试'], 'data': {'url': 'https://chat.qwen.ai:443//api/v2/chat/completio |
| `qwen3.5-122b-a10b` | image | ❌ `http_error` | 0.90s | RuntimeError: Response: {'success': False, 'request_id': '7bce8a39-fa24-4408-9e53-45d11ce9af77', 'data': {'code': 'Not_Found', 'details': 'Model not found'}} |
| `qwen3.5-27b` | image | ❌ `http_error` | 0.80s | RuntimeError: Response: {'success': False, 'request_id': '1eaea692-7f7e-48bb-80d6-42d4cdb86724', 'data': {'code': 'Not_Found', 'details': 'Model not found'}} |
| `qwen3.5-35b-a3b` | image | ❌ `http_error` | 0.87s | RuntimeError: Response: {'success': False, 'request_id': '3d8573f3-0b0c-4a80-aff4-ff5d39680a58', 'data': {'code': 'Not_Found', 'details': 'Model not found'}} |
| `qwen3.5-397b-a17b` | image | ❌ `exception` | 41.45s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-flash` | image | ❌ `exception` | 41.08s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-max-2026-03-08` | text | ❌ `http_error` | 0.85s | RuntimeError: Response: {'success': False, 'request_id': 'a3779df3-08ba-499e-bf3b-44d50343607c', 'data': {'code': 'Not_Found', 'details': 'Model not found'}} |
| `qwen3.5-omni-flash` | image | ❌ `timeout` | 63.07s | Timeout limit exceeded |
| `qwen3.5-omni-plus` | image | ❌ `exception` | 41.17s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-plus` | image | ❌ `exception` | 21.02s | NoMediaResponseError: No media response from Qwen |
| `qwen3.6-27b` | image | ❌ `exception` | 4.10s | NoMediaResponseError: No media response from Qwen |
| `qwen3.6-35b-a3b` | image | ❌ `exception` | 22.02s | NoMediaResponseError: No media response from Qwen |
| `qwen3.6-plus` | image | ❌ `exception` | 21.02s | NoMediaResponseError: No media response from Qwen |
| `qwen3.6-plus-preview` | text | ❌ `http_error` | 1.07s | RuntimeError: Response: {'success': False, 'request_id': 'ac05641b-1585-4e0e-a02c-8b124e30b3e5', 'data': {'code': 'Not_Found', 'details': 'Model not found'}} |
| `qwen3.7-max` | image | ❌ `exception` | 41.40s | NoMediaResponseError: No media response from Qwen |
| `qwen3.7-plus` | image | ❌ `exception` | 22.03s | NoMediaResponseError: No media response from Qwen |

## Sample successful responses

### `qwen3.6-max-preview` — text

```
PONG
```

