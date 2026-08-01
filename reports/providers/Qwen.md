# Qwen

- **Label:** Qwen
- **URL:** https://chat.qwen.ai
- **Models:** 23
- **Working tests:** 1 / 23
- **Avg response time:** 22.50s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `qwen3.6-max-preview` | text | ✅ `ok` | 22.50s | contains expected token 'PONG' |
| `qwen-latest-series-invite-beta-v16` | text | ❌ `rate_limited` | 0.82s | RuntimeError: Response: {'success': False, 'request_id': '44d4236b-a429-4587-b55c-c6c65db074ab', 'data': {'code': 'Not_Found', 'details': 'Model not found'}} |
| `qwen-latest-series-invite-beta-v24` | text | ❌ `http_error` | 0.93s | RuntimeError: Response: {'success': False, 'request_id': 'bd77e06b-4369-434b-9964-1df9236c5458', 'data': {'code': 'Not_Found', 'details': 'Model not found'}} |
| `qwen-plus-2025-07-28` | image | ❌ `exception` | 41.52s | NoMediaResponseError: No media response from Qwen |
| `qwen3-coder-plus` | image | ❌ `exception` | 41.35s | NoMediaResponseError: No media response from Qwen |
| `qwen3-max-2026-01-23` | image | ❌ `exception` | 41.32s | NoMediaResponseError: No media response from Qwen |
| `qwen3-omni-flash-2025-12-01` | image | ❌ `exception` | 21.04s | NoMediaResponseError: No media response from Qwen |
| `qwen3-vl-plus` | image | ❌ `exception` | 22.03s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-122b-a10b` | image | ❌ `http_error` | 0.89s | RuntimeError: Response: {'success': False, 'request_id': 'd15eb72a-6b74-4679-9b33-b59fe86a7461', 'data': {'code': 'Not_Found', 'details': 'Model not found'}} |
| `qwen3.5-27b` | image | ❌ `http_error` | 0.86s | RuntimeError: Response: {'success': False, 'request_id': '52b49c69-da3f-49a8-823b-b4e4dd8b7a35', 'data': {'code': 'Not_Found', 'details': 'Model not found'}} |
| `qwen3.5-35b-a3b` | image | ❌ `http_error` | 0.91s | RuntimeError: Response: {'success': False, 'request_id': '58bed10f-7a6e-4059-bbb6-26ebe674b319', 'data': {'code': 'Not_Found', 'details': 'Model not found'}} |
| `qwen3.5-397b-a17b` | image | ❌ `exception` | 21.68s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-flash` | image | ❌ `exception` | 41.28s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-max-2026-03-08` | text | ❌ `http_error` | 0.96s | RuntimeError: Response: {'success': False, 'request_id': '8a483d76-54d3-4627-9634-813ed9809fda', 'data': {'code': 'Not_Found', 'details': 'Model not found'}} |
| `qwen3.5-omni-flash` | image | ❌ `timeout` | 64.59s | Timeout limit exceeded |
| `qwen3.5-omni-plus` | image | ❌ `exception` | 41.29s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-plus` | image | ❌ `exception` | 41.31s | NoMediaResponseError: No media response from Qwen |
| `qwen3.6-27b` | image | ❌ `exception` | 21.03s | NoMediaResponseError: No media response from Qwen |
| `qwen3.6-35b-a3b` | image | ❌ `exception` | 22.02s | NoMediaResponseError: No media response from Qwen |
| `qwen3.6-plus` | image | ❌ `exception` | 21.03s | NoMediaResponseError: No media response from Qwen |
| `qwen3.6-plus-preview` | text | ❌ `http_error` | 0.89s | RuntimeError: Response: {'success': False, 'request_id': 'ca4a40d6-dac3-4d06-95a1-7912aa47a895', 'data': {'code': 'Not_Found', 'details': 'Model not found'}} |
| `qwen3.7-max` | image | ❌ `exception` | 21.03s | NoMediaResponseError: No media response from Qwen |
| `qwen3.7-plus` | image | ❌ `exception` | 22.03s | NoMediaResponseError: No media response from Qwen |

## Sample successful responses

### `qwen3.6-max-preview` — text

```
PONG
```

