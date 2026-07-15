# Qwen

- **Label:** Qwen
- **URL:** https://chat.qwen.ai
- **Models:** 23
- **Working tests:** 2 / 23
- **Avg response time:** 4.47s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `qwen3.5-max-2026-03-08` | text | ✅ `ok` | 2.78s | contains expected token 'PONG' |
| `qwen3.6-max-preview` | text | ✅ `ok` | 6.15s | contains expected token 'PONG' |
| `qwen-latest-series-invite-beta-v16` | text | ❌ `http_error` | 0.84s | RuntimeError: Response: {'success': False, 'request_id': '417f576b-7910-4954-99a6-46460aa4b1e8', 'data': {'code': 'Not_Found', 'details': 'Model not found'}} |
| `qwen-latest-series-invite-beta-v24` | text | ❌ `http_error` | 0.76s | RuntimeError: Response: {'success': False, 'request_id': '3beda72f-4dda-4e6b-9d5a-299a32a3b471', 'data': {'code': 'Not_Found', 'details': 'Model not found'}} |
| `qwen-plus-2025-07-28` | image | ❌ `exception` | 4.28s | NoMediaResponseError: No media response from Qwen |
| `qwen3-coder-plus` | image | ❌ `exception` | 6.80s | NoMediaResponseError: No media response from Qwen |
| `qwen3-max-2026-01-23` | image | ❌ `exception` | 11.56s | NoMediaResponseError: No media response from Qwen |
| `qwen3-omni-flash-2025-12-01` | image | ❌ `exception` | 10.16s | NoMediaResponseError: No media response from Qwen |
| `qwen3-vl-plus` | image | ❌ `exception` | 9.52s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-122b-a10b` | image | ❌ `http_error` | 0.93s | RuntimeError: Response: {'success': False, 'request_id': 'f9c67fbc-f5a3-4349-afdd-648daf6650b0', 'data': {'code': 'Not_Found', 'details': 'Model not found'}} |
| `qwen3.5-27b` | image | ❌ `http_error` | 0.81s | RuntimeError: Response: {'success': False, 'request_id': '5720d202-44bb-438b-a726-dcf9f775307a', 'data': {'code': 'Not_Found', 'details': 'Model not found'}} |
| `qwen3.5-35b-a3b` | image | ❌ `http_error` | 0.87s | RuntimeError: Response: {'success': False, 'request_id': 'bcb092ac-ecee-44d9-b50e-878c2ac6d089', 'data': {'code': 'Not_Found', 'details': 'Model not found'}} |
| `qwen3.5-397b-a17b` | image | ❌ `exception` | 4.45s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-flash` | image | ❌ `exception` | 2.68s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-omni-flash` | image | ❌ `exception` | 6.62s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-omni-plus` | image | ❌ `exception` | 3.99s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-plus` | image | ❌ `exception` | 10.25s | NoMediaResponseError: No media response from Qwen |
| `qwen3.6-27b` | image | ❌ `exception` | 3.26s | NoMediaResponseError: No media response from Qwen |
| `qwen3.6-35b-a3b` | image | ❌ `exception` | 8.36s | NoMediaResponseError: No media response from Qwen |
| `qwen3.6-plus` | image | ❌ `exception` | 12.34s | NoMediaResponseError: No media response from Qwen |
| `qwen3.6-plus-preview` | text | ❌ `http_error` | 0.78s | RuntimeError: Response: {'success': False, 'request_id': '48e8f56a-8ff2-44ad-adbc-bba1bd5b93e1', 'data': {'code': 'Not_Found', 'details': 'Model not found'}} |
| `qwen3.7-max` | image | ❌ `exception` | 8.94s | NoMediaResponseError: No media response from Qwen |
| `qwen3.7-plus` | image | ❌ `exception` | 10.17s | NoMediaResponseError: No media response from Qwen |

## Sample successful responses

### `qwen3.6-max-preview` — text

```
PONG
```

### `qwen3.5-max-2026-03-08` — text

```
PONG
```

