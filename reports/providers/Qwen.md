# Qwen

- **Label:** Qwen
- **URL:** https://chat.qwen.ai
- **Models:** 23
- **Working tests:** 1 / 23
- **Avg response time:** 2.59s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `qwen3.6-max-preview` | text | ✅ `ok` | 2.59s | contains expected token 'PONG' |
| `qwen-latest-series-invite-beta-v16` | text | ❌ `http_error` | 0.92s | RuntimeError: Response: {'success': False, 'request_id': '1c5ed0cc-4b7b-4c4a-9805-d5abe7bdced7', 'data': {'code': 'Not_Found', 'details': 'Model not found'}} |
| `qwen-latest-series-invite-beta-v24` | text | ❌ `http_error` | 0.85s | RuntimeError: Response: {'success': False, 'request_id': '559147ed-6336-4989-bd14-c423ae39cd6e', 'data': {'code': 'Not_Found', 'details': 'Model not found'}} |
| `qwen-plus-2025-07-28` | image | ❌ `exception` | 6.16s | NoMediaResponseError: No media response from Qwen |
| `qwen3-coder-plus` | image | ❌ `exception` | 4.81s | NoMediaResponseError: No media response from Qwen |
| `qwen3-max-2026-01-23` | image | ❌ `exception` | 9.36s | NoMediaResponseError: No media response from Qwen |
| `qwen3-omni-flash-2025-12-01` | image | ❌ `exception` | 11.69s | NoMediaResponseError: No media response from Qwen |
| `qwen3-vl-plus` | image | ❌ `exception` | 8.34s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-122b-a10b` | image | ❌ `http_error` | 0.97s | RuntimeError: Response: {'success': False, 'request_id': '37b40a44-2828-49ab-8e6e-ef454456cdc0', 'data': {'code': 'Not_Found', 'details': 'Model not found'}} |
| `qwen3.5-27b` | image | ❌ `http_error` | 1.05s | RuntimeError: Response: {'success': False, 'request_id': '677be9ef-10f1-496a-859c-9e9a94c7e56d', 'data': {'code': 'Not_Found', 'details': 'Model not found'}} |
| `qwen3.5-35b-a3b` | image | ❌ `http_error` | 0.82s | RuntimeError: Response: {'success': False, 'request_id': 'ef317ce6-2907-4464-a743-0caca7334d12', 'data': {'code': 'Not_Found', 'details': 'Model not found'}} |
| `qwen3.5-397b-a17b` | image | ❌ `exception` | 4.96s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-flash` | image | ❌ `exception` | 2.42s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-max-2026-03-08` | text | ❌ `http_error` | 1.03s | RuntimeError: Response: {'success': False, 'request_id': '791c9abc-1cdd-45d1-9b00-d288940436fe', 'data': {'code': 'Not_Found', 'details': 'Model not found'}} |
| `qwen3.5-omni-flash` | image | ❌ `exception` | 9.82s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-omni-plus` | image | ❌ `exception` | 4.68s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-plus` | image | ❌ `exception` | 10.51s | NoMediaResponseError: No media response from Qwen |
| `qwen3.6-27b` | image | ❌ `exception` | 4.07s | NoMediaResponseError: No media response from Qwen |
| `qwen3.6-35b-a3b` | image | ❌ `exception` | 8.38s | NoMediaResponseError: No media response from Qwen |
| `qwen3.6-plus` | image | ❌ `exception` | 11.34s | NoMediaResponseError: No media response from Qwen |
| `qwen3.6-plus-preview` | text | ❌ `http_error` | 0.83s | RuntimeError: Response: {'success': False, 'request_id': 'b0a42893-d44c-46de-b056-7a456e265662', 'data': {'code': 'Not_Found', 'details': 'Model not found'}} |
| `qwen3.7-max` | image | ❌ `exception` | 9.21s | NoMediaResponseError: No media response from Qwen |
| `qwen3.7-plus` | image | ❌ `exception` | 13.07s | NoMediaResponseError: No media response from Qwen |

## Sample successful responses

### `qwen3.6-max-preview` — text

```
PONG
```

