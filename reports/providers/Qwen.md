# Qwen

- **Label:** Qwen
- **URL:** https://chat.qwen.ai
- **Models:** 23
- **Working tests:** 0 / 23
- **Avg response time:** —

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `qwen-latest-series-invite-beta-v16` | text | ❌ `http_error` | 0.89s | RuntimeError: Response: {'success': False, 'request_id': '1571168b-c11e-455d-8396-763e00de93a2', 'data': {'code': 'Not_Found', 'details': 'Model not found'}} |
| `qwen-latest-series-invite-beta-v24` | text | ❌ `exception` | 0.95s | RuntimeError: Response: {'ret': ['FAIL_SYS_USER_VALIDATE', 'RGV587_ERROR::SM::哎哟喂,被挤爆啦,请稍后重试'], 'data': {'url': 'https://chat.qwen.ai:443//api/v2/chat/completio |
| `qwen-plus-2025-07-28` | image | ❌ `exception` | 0.96s | RuntimeError: Response: {'ret': ['FAIL_SYS_USER_VALIDATE', 'RGV587_ERROR::SM::哎哟喂,被挤爆啦,请稍后重试'], 'data': {'url': 'https://chat.qwen.ai:443//api/v2/chat/completio |
| `qwen3-coder-plus` | image | ❌ `exception` | 21.02s | NoMediaResponseError: No media response from Qwen |
| `qwen3-max-2026-01-23` | image | ❌ `exception` | 1.04s | RuntimeError: Response: {'ret': ['FAIL_SYS_USER_VALIDATE', 'RGV587_ERROR::SM::哎哟喂,被挤爆啦,请稍后重试'], 'data': {'url': 'https://chat.qwen.ai:443//api/v2/chat/completio |
| `qwen3-omni-flash-2025-12-01` | image | ❌ `exception` | 22.14s | NoMediaResponseError: No media response from Qwen |
| `qwen3-vl-plus` | image | ❌ `exception` | 0.95s | RuntimeError: Response: {'ret': ['FAIL_SYS_USER_VALIDATE', 'RGV587_ERROR::SM::哎哟喂,被挤爆啦,请稍后重试'], 'data': {'url': 'https://chat.qwen.ai:443//api/v2/chat/completio |
| `qwen3.5-122b-a10b` | image | ❌ `http_error` | 20.97s | RuntimeError: Response: {'success': False, 'request_id': '12323d70-685e-4282-8ece-797cc079a362', 'data': {'code': 'Not_Found', 'details': 'Model not found'}} |
| `qwen3.5-27b` | image | ❌ `http_error` | 0.91s | RuntimeError: Response: {'success': False, 'request_id': '51ca093e-fac9-454d-9fc5-ff259696b35c', 'data': {'code': 'Not_Found', 'details': 'Model not found'}} |
| `qwen3.5-35b-a3b` | image | ❌ `http_error` | 0.98s | RuntimeError: Response: {'success': False, 'request_id': 'a3995ae0-b785-4103-a08d-dbd2915037ef', 'data': {'code': 'Not_Found', 'details': 'Model not found'}} |
| `qwen3.5-397b-a17b` | image | ❌ `exception` | 0.89s | RuntimeError: Response: {'ret': ['FAIL_SYS_USER_VALIDATE', 'RGV587_ERROR::SM::哎哟喂,被挤爆啦,请稍后重试'], 'data': {'url': 'https://chat.qwen.ai:443//api/v2/chat/completio |
| `qwen3.5-flash` | image | ❌ `http_error` | 43.20s | RuntimeError: Response: {'ret': ['FAIL_SYS_USER_VALIDATE', 'RGV587_ERROR::SM::哎哟喂,被挤爆啦,请稍后重试'], 'data': {'url': 'https://chat.qwen.ai:443//api/v2/chat/completio |
| `qwen3.5-max-2026-03-08` | text | ❌ `http_error` | 1.08s | RuntimeError: Response: {'success': False, 'request_id': '7c40f154-8ac2-4b50-8baa-9ca399bf0856', 'data': {'code': 'Not_Found', 'details': 'Model not found'}} |
| `qwen3.5-omni-flash` | image | ❌ `exception` | 21.02s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-omni-plus` | image | ❌ `http_error` | 1.17s | RuntimeError: Response: {'ret': ['FAIL_SYS_USER_VALIDATE', 'RGV587_ERROR::SM::哎哟喂,被挤爆啦,请稍后重试'], 'data': {'url': 'https://chat.qwen.ai:443//api/v2/chat/completio |
| `qwen3.5-plus` | image | ❌ `exception` | 1.01s | RuntimeError: Response: {'ret': ['FAIL_SYS_USER_VALIDATE', 'RGV587_ERROR::SM::哎哟喂,被挤爆啦,请稍后重试'], 'data': {'url': 'https://chat.qwen.ai:443//api/v2/chat/completio |
| `qwen3.6-27b` | image | ❌ `exception` | 21.03s | NoMediaResponseError: No media response from Qwen |
| `qwen3.6-35b-a3b` | image | ❌ `exception` | 21.03s | NoMediaResponseError: No media response from Qwen |
| `qwen3.6-max-preview` | text | ❌ `exception` | 1.05s | RuntimeError: Response: {'ret': ['FAIL_SYS_USER_VALIDATE', 'RGV587_ERROR::SM::哎哟喂,被挤爆啦,请稍后重试'], 'data': {'url': 'https://chat.qwen.ai:443//api/v2/chat/completio |
| `qwen3.6-plus` | image | ❌ `exception` | 22.02s | NoMediaResponseError: No media response from Qwen |
| `qwen3.6-plus-preview` | text | ❌ `http_error` | 0.97s | RuntimeError: Response: {'success': False, 'request_id': 'f2fad16a-f7d7-4094-8372-6757644fc9cf', 'data': {'code': 'Not_Found', 'details': 'Model not found'}} |
| `qwen3.7-max` | image | ❌ `exception` | 0.97s | RuntimeError: Response: {'ret': ['FAIL_SYS_USER_VALIDATE', 'RGV587_ERROR::SM::哎哟喂,被挤爆啦,请稍后重试'], 'data': {'url': 'https://chat.qwen.ai:443//api/v2/chat/completio |
| `qwen3.7-plus` | image | ❌ `exception` | 22.03s | NoMediaResponseError: No media response from Qwen |
