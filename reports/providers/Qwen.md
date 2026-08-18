# Qwen

- **Label:** Qwen
- **URL:** https://chat.qwen.ai
- **Models:** 23
- **Working tests:** 1 / 23
- **Avg response time:** 22.09s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `qwen3.6-max-preview` | text | ✅ `ok` | 22.09s | contains expected token 'PONG' |
| `qwen-latest-series-invite-beta-v16` | text | ❌ `http_error` | 1.18s | RuntimeError: Response: {'success': False, 'request_id': '20f1d74c-1210-4328-9600-ccc8b0be75ef', 'data': {'code': 'Not_Found', 'details': 'Model not found'}} |
| `qwen-latest-series-invite-beta-v24` | text | ❌ `http_error` | 0.89s | RuntimeError: Response: {'success': False, 'request_id': 'b2cff46b-f003-4e64-af99-ff3caaf9203d', 'data': {'code': 'Not_Found', 'details': 'Model not found'}} |
| `qwen-plus-2025-07-28` | image | ❌ `exception` | 20.72s | RuntimeError: Response: {'ret': ['FAIL_SYS_USER_VALIDATE', 'RGV587_ERROR::SM::哎哟喂,被挤爆啦,请稍后重试'], 'data': {'url': 'https://chat.qwen.ai:443//api/v2/chat/completio |
| `qwen3-coder-plus` | image | ❌ `exception` | 21.02s | NoMediaResponseError: No media response from Qwen |
| `qwen3-max-2026-01-23` | image | ❌ `exception` | 0.95s | RuntimeError: Response: {'ret': ['FAIL_SYS_USER_VALIDATE', 'RGV587_ERROR::SM::哎哟喂,被挤爆啦,请稍后重试'], 'data': {'url': 'https://chat.qwen.ai:443//api/v2/chat/completio |
| `qwen3-omni-flash-2025-12-01` | image | ❌ `exception` | 22.02s | NoMediaResponseError: No media response from Qwen |
| `qwen3-vl-plus` | image | ❌ `exception` | 22.74s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-122b-a10b` | image | ❌ `http_error` | 0.91s | RuntimeError: Response: {'success': False, 'request_id': '587148f2-b6ed-4f87-a8ce-1362013ff9c0', 'data': {'code': 'Not_Found', 'details': 'Model not found'}} |
| `qwen3.5-27b` | image | ❌ `exception` | 0.87s | RuntimeError: Response: {'ret': ['FAIL_SYS_USER_VALIDATE', 'RGV587_ERROR::SM::哎哟喂,被挤爆啦,请稍后重试'], 'data': {'url': 'https://chat.qwen.ai:443//api/v2/chat/completio |
| `qwen3.5-35b-a3b` | image | ❌ `exception` | 0.88s | RuntimeError: Response: {'ret': ['FAIL_SYS_USER_VALIDATE', 'RGV587_ERROR::SM::哎哟喂,被挤爆啦,请稍后重试'], 'data': {'url': 'https://chat.qwen.ai:443//api/v2/chat/completio |
| `qwen3.5-397b-a17b` | image | ❌ `exception` | 22.11s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-flash` | image | ❌ `exception` | 41.39s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-max-2026-03-08` | text | ❌ `http_error` | 0.88s | RuntimeError: Response: {'success': False, 'request_id': '833f1eab-acb1-4a77-ae75-56c34e7375ed', 'data': {'code': 'Not_Found', 'details': 'Model not found'}} |
| `qwen3.5-omni-flash` | image | ❌ `exception` | 0.91s | RuntimeError: Response: {'ret': ['FAIL_SYS_USER_VALIDATE', 'RGV587_ERROR::SM::哎哟喂,被挤爆啦,请稍后重试'], 'data': {'url': 'https://chat.qwen.ai:443//api/v2/chat/completio |
| `qwen3.5-omni-plus` | image | ❌ `exception` | 22.03s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-plus` | image | ❌ `exception` | 0.88s | RuntimeError: Response: {'ret': ['FAIL_SYS_USER_VALIDATE', 'RGV587_ERROR::SM::哎哟喂,被挤爆啦,请稍后重试'], 'data': {'url': 'https://chat.qwen.ai:443//api/v2/chat/completio |
| `qwen3.6-27b` | image | ❌ `exception` | 0.98s | RuntimeError: Response: {'ret': ['FAIL_SYS_USER_VALIDATE', 'RGV587_ERROR::SM::哎哟喂,被挤爆啦,请稍后重试'], 'data': {'url': 'https://chat.qwen.ai:443//api/v2/chat/completio |
| `qwen3.6-35b-a3b` | image | ❌ `exception` | 41.35s | NoMediaResponseError: No media response from Qwen |
| `qwen3.6-plus` | image | ❌ `exception` | 41.50s | NoMediaResponseError: No media response from Qwen |
| `qwen3.6-plus-preview` | text | ❌ `http_error` | 0.96s | RuntimeError: Response: {'success': False, 'request_id': 'd275178b-c6e0-4d84-bbc7-3d4b0d1bc064', 'data': {'code': 'Not_Found', 'details': 'Model not found'}} |
| `qwen3.7-max` | image | ❌ `exception` | 41.32s | NoMediaResponseError: No media response from Qwen |
| `qwen3.7-plus` | image | ❌ `exception` | 22.01s | NoMediaResponseError: No media response from Qwen |

## Sample successful responses

### `qwen3.6-max-preview` — text

```
PONG
```

