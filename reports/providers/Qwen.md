# Qwen

- **Label:** Qwen
- **URL:** https://chat.qwen.ai
- **Models:** 23
- **Working tests:** 1 / 23
- **Avg response time:** 21.92s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `qwen3.6-max-preview` | text | ✅ `ok` | 21.92s | contains expected token 'PONG' |
| `qwen-latest-series-invite-beta-v16` | text | ❌ `rate_limited` | 0.83s | RuntimeError: Response: {'success': False, 'request_id': '6052666d-f9c7-43fe-8ffa-b6908c684299', 'data': {'code': 'Not_Found', 'details': 'Model not found'}} |
| `qwen-latest-series-invite-beta-v24` | text | ❌ `http_error` | 0.71s | RuntimeError: Response: {'success': False, 'request_id': 'ab6632f5-7ee9-4e8b-8d67-69d5080bce17', 'data': {'code': 'Not_Found', 'details': 'Model not found'}} |
| `qwen-plus-2025-07-28` | image | ❌ `exception` | 41.30s | NoMediaResponseError: No media response from Qwen |
| `qwen3-coder-plus` | image | ❌ `exception` | 41.11s | NoMediaResponseError: No media response from Qwen |
| `qwen3-max-2026-01-23` | image | ❌ `exception` | 43.05s | RuntimeError: Response: {'ret': ['FAIL_SYS_USER_VALIDATE', 'RGV587_ERROR::SM::哎哟喂,被挤爆啦,请稍后重试'], 'data': {'url': 'https://chat.qwen.ai:443//api/v2/chat/completio |
| `qwen3-omni-flash-2025-12-01` | image | ❌ `exception` | 20.46s | NoMediaResponseError: No media response from Qwen |
| `qwen3-vl-plus` | image | ❌ `exception` | 0.76s | RuntimeError: Response: {'ret': ['FAIL_SYS_USER_VALIDATE', 'RGV587_ERROR::SM::哎哟喂,被挤爆啦,请稍后重试'], 'data': {'url': 'https://chat.qwen.ai:443//api/v2/chat/completio |
| `qwen3.5-122b-a10b` | image | ❌ `http_error` | 0.76s | RuntimeError: Response: {'success': False, 'request_id': 'fd664ae6-14a0-4243-8e6d-e1a420faf033', 'data': {'code': 'Not_Found', 'details': 'Model not found'}} |
| `qwen3.5-27b` | image | ❌ `http_error` | 0.80s | RuntimeError: Response: {'success': False, 'request_id': 'f63157a9-fa98-48b9-9a49-8ab9ed164423', 'data': {'code': 'Not_Found', 'details': 'Model not found'}} |
| `qwen3.5-35b-a3b` | image | ❌ `http_error` | 0.64s | RuntimeError: Response: {'success': False, 'request_id': 'cdb9f681-0a66-46c0-a8dc-38f93712fd27', 'data': {'code': 'Not_Found', 'details': 'Model not found'}} |
| `qwen3.5-397b-a17b` | image | ❌ `exception` | 41.31s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-flash` | image | ❌ `exception` | 22.02s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-max-2026-03-08` | text | ❌ `http_error` | 0.75s | RuntimeError: Response: {'success': False, 'request_id': 'bca244e3-b2ef-4536-8cf7-ae1a5c295940', 'data': {'code': 'Not_Found', 'details': 'Model not found'}} |
| `qwen3.5-omni-flash` | image | ❌ `exception` | 22.02s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-omni-plus` | image | ❌ `exception` | 0.66s | RuntimeError: Response: {'ret': ['FAIL_SYS_USER_VALIDATE', 'RGV587_ERROR::SM::哎哟喂,被挤爆啦,请稍后重试'], 'data': {'url': 'https://chat.qwen.ai:443//api/v2/chat/completio |
| `qwen3.5-plus` | image | ❌ `exception` | 41.48s | NoMediaResponseError: No media response from Qwen |
| `qwen3.6-27b` | image | ❌ `exception` | 41.43s | NoMediaResponseError: No media response from Qwen |
| `qwen3.6-35b-a3b` | image | ❌ `exception` | 22.02s | NoMediaResponseError: No media response from Qwen |
| `qwen3.6-plus` | image | ❌ `exception` | 41.30s | NoMediaResponseError: No media response from Qwen |
| `qwen3.6-plus-preview` | text | ❌ `http_error` | 0.69s | RuntimeError: Response: {'success': False, 'request_id': '3316a07e-e527-40c2-9493-315af4abdad8', 'data': {'code': 'Not_Found', 'details': 'Model not found'}} |
| `qwen3.7-max` | image | ❌ `exception` | 41.39s | NoMediaResponseError: No media response from Qwen |
| `qwen3.7-plus` | image | ❌ `exception` | 22.02s | NoMediaResponseError: No media response from Qwen |

## Sample successful responses

### `qwen3.6-max-preview` — text

```
PONG
```

