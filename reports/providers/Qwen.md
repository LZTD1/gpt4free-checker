# Qwen

- **Label:** Qwen
- **URL:** https://chat.qwen.ai
- **Models:** 23
- **Working tests:** 1 / 23
- **Avg response time:** 3.19s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `qwen3.6-max-preview` | text | ✅ `ok` | 3.19s | contains expected token 'PONG' |
| `qwen-latest-series-invite-beta-v16` | text | ❌ `http_error` | 0.78s | RuntimeError: Response: {'success': False, 'request_id': '75662ddb-2c11-44e4-8c0f-1c47a617b0ed', 'data': {'code': 'Not_Found', 'details': 'Model not found'}} |
| `qwen-latest-series-invite-beta-v24` | text | ❌ `http_error` | 0.79s | RuntimeError: Response: {'success': False, 'request_id': '27a9ed06-ed22-46ef-9eb3-1bd3004d89cf', 'data': {'code': 'Not_Found', 'details': 'Model not found'}} |
| `qwen-plus-2025-07-28` | image | ❌ `exception` | 6.41s | NoMediaResponseError: No media response from Qwen |
| `qwen3-coder-plus` | image | ❌ `exception` | 5.04s | NoMediaResponseError: No media response from Qwen |
| `qwen3-max-2026-01-23` | image | ❌ `exception` | 8.09s | NoMediaResponseError: No media response from Qwen |
| `qwen3-omni-flash-2025-12-01` | image | ❌ `exception` | 7.91s | NoMediaResponseError: No media response from Qwen |
| `qwen3-vl-plus` | image | ❌ `exception` | 9.38s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-122b-a10b` | image | ❌ `http_error` | 0.94s | RuntimeError: Response: {'success': False, 'request_id': 'a2182ac4-734a-4a47-a540-b48776e1328a', 'data': {'code': 'Not_Found', 'details': 'Model not found'}} |
| `qwen3.5-27b` | image | ❌ `http_error` | 0.84s | RuntimeError: Response: {'success': False, 'request_id': '993b7a77-55f0-4f72-a1e7-360b2e49a5d3', 'data': {'code': 'Not_Found', 'details': 'Model not found'}} |
| `qwen3.5-35b-a3b` | image | ❌ `http_error` | 0.88s | RuntimeError: Response: {'success': False, 'request_id': '2f6f6d47-f5c2-464a-967d-c5fb9a99520e', 'data': {'code': 'Not_Found', 'details': 'Model not found'}} |
| `qwen3.5-397b-a17b` | image | ❌ `exception` | 8.53s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-flash` | image | ❌ `exception` | 3.02s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-max-2026-03-08` | text | ❌ `timeout` | 62.81s | Timeout limit exceeded |
| `qwen3.5-omni-flash` | image | ❌ `exception` | 6.80s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-omni-plus` | image | ❌ `exception` | 5.05s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-plus` | image | ❌ `exception` | 10.42s | NoMediaResponseError: No media response from Qwen |
| `qwen3.6-27b` | image | ❌ `exception` | 5.21s | NoMediaResponseError: No media response from Qwen |
| `qwen3.6-35b-a3b` | image | ❌ `exception` | 9.69s | NoMediaResponseError: No media response from Qwen |
| `qwen3.6-plus` | image | ❌ `exception` | 14.99s | NoMediaResponseError: No media response from Qwen |
| `qwen3.6-plus-preview` | text | ❌ `http_error` | 0.85s | RuntimeError: Response: {'success': False, 'request_id': 'd715413e-216b-4e7b-bb57-ed995d93a189', 'data': {'code': 'Not_Found', 'details': 'Model not found'}} |
| `qwen3.7-max` | image | ❌ `exception` | 9.09s | NoMediaResponseError: No media response from Qwen |
| `qwen3.7-plus` | image | ❌ `exception` | 10.09s | NoMediaResponseError: No media response from Qwen |

## Sample successful responses

### `qwen3.6-max-preview` — text

```
PONG
```

