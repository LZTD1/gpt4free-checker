# Qwen

- **Label:** Qwen
- **URL:** https://chat.qwen.ai
- **Models:** 23
- **Working tests:** 2 / 23
- **Avg response time:** 7.99s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `qwen3.5-max-2026-03-08` | text | ✅ `ok` | 11.16s | contains expected token 'PONG' |
| `qwen3.6-max-preview` | text | ✅ `ok` | 4.81s | contains expected token 'PONG' |
| `qwen-latest-series-invite-beta-v16` | text | ❌ `http_error` | 0.86s | RuntimeError: Response: {'success': False, 'request_id': 'a85457e7-4019-494b-bf67-00f918b15062', 'data': {'code': 'Not_Found', 'details': 'Model not found'}} |
| `qwen-latest-series-invite-beta-v24` | text | ❌ `http_error` | 0.86s | RuntimeError: Response: {'success': False, 'request_id': 'fdbbfda7-818a-4485-b3a5-83df1f0acf71', 'data': {'code': 'Not_Found', 'details': 'Model not found'}} |
| `qwen-plus-2025-07-28` | image | ❌ `exception` | 15.87s | NoMediaResponseError: No media response from Qwen |
| `qwen3-coder-plus` | image | ❌ `exception` | 17.47s | NoMediaResponseError: No media response from Qwen |
| `qwen3-max-2026-01-23` | image | ❌ `exception` | 8.58s | NoMediaResponseError: No media response from Qwen |
| `qwen3-omni-flash-2025-12-01` | image | ❌ `exception` | 31.72s | NoMediaResponseError: No media response from Qwen |
| `qwen3-vl-plus` | image | ❌ `timeout` | 82.48s | Timeout limit exceeded |
| `qwen3.5-122b-a10b` | image | ❌ `http_error` | 1.04s | RuntimeError: Response: {'success': False, 'request_id': 'e31c0b43-3a8b-4321-86df-bfd4d46401ad', 'data': {'code': 'Not_Found', 'details': 'Model not found'}} |
| `qwen3.5-27b` | image | ❌ `http_error` | 0.96s | RuntimeError: Response: {'success': False, 'request_id': '00356efe-4af6-41c5-8986-97eba03ef0e2', 'data': {'code': 'Not_Found', 'details': 'Model not found'}} |
| `qwen3.5-35b-a3b` | image | ❌ `http_error` | 0.84s | RuntimeError: Response: {'success': False, 'request_id': '1ff36366-4881-402c-963b-507d56445f43', 'data': {'code': 'Not_Found', 'details': 'Model not found'}} |
| `qwen3.5-397b-a17b` | image | ❌ `exception` | 28.11s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-flash` | image | ❌ `exception` | 7.86s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-omni-flash` | image | ❌ `exception` | 15.42s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-omni-plus` | image | ❌ `exception` | 16.59s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-plus` | image | ❌ `exception` | 12.22s | NoMediaResponseError: No media response from Qwen |
| `qwen3.6-27b` | image | ❌ `exception` | 18.70s | NoMediaResponseError: No media response from Qwen |
| `qwen3.6-35b-a3b` | image | ❌ `exception` | 10.20s | NoMediaResponseError: No media response from Qwen |
| `qwen3.6-plus` | image | ❌ `exception` | 11.73s | NoMediaResponseError: No media response from Qwen |
| `qwen3.6-plus-preview` | text | ❌ `http_error` | 0.97s | RuntimeError: Response: {'success': False, 'request_id': '48957718-0daf-4f00-9fd4-fdd7da0d1fa7', 'data': {'code': 'Not_Found', 'details': 'Model not found'}} |
| `qwen3.7-max` | image | ❌ `exception` | 11.07s | NoMediaResponseError: No media response from Qwen |
| `qwen3.7-plus` | image | ❌ `exception` | 19.50s | NoMediaResponseError: No media response from Qwen |

## Sample successful responses

### `qwen3.6-max-preview` — text

```
PONG
```

### `qwen3.5-max-2026-03-08` — text

```
PONG
```

