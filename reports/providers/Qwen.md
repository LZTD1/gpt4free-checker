# Qwen

- **Label:** Qwen
- **URL:** https://chat.qwen.ai
- **Models:** 19
- **Working tests:** 3 / 19
- **Avg response time:** 8.25s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `qwen3.5-max-2026-03-08` | text | ✅ `ok` | 9.84s | contains expected token 'PONG' |
| `qwen3.6-max-preview` | text | ✅ `ok` | 6.79s | contains expected token 'PONG' |
| `qwen3.6-plus-preview` | text | ✅ `ok` | 8.13s | contains expected token 'PONG' |
| `qwen-max-latest` | image | ❌ `http_error` | 24.01s | RuntimeError: Response: {'success': False, 'request_id': 'a4012b43-4c34-40d2-aa20-f8ffe1074753', 'data': {'code': 'Not_Found', 'details': 'Model not found'}} |
| `qwen-plus-2025-07-28` | image | ❌ `exception` | 20.01s | NoMediaResponseError: No media response from Qwen |
| `qwen3-coder-plus` | image | ❌ `exception` | 33.89s | NoMediaResponseError: No media response from Qwen |
| `qwen3-max-2026-01-23` | image | ❌ `exception` | 25.96s | NoMediaResponseError: No media response from Qwen |
| `qwen3-omni-flash-2025-12-01` | image | ❌ `exception` | 18.13s | ResponseError: internal_error: Allocated quota exceeded, please increase your quota limit. For details, see: https://www.alibabacloud.com/help/en/model-studio/e |
| `qwen3-vl-plus` | image | ❌ `timeout` | 45.66s | Timeout limit exceeded |
| `qwen3.5-122b-a10b` | image | ❌ `exception` | 23.16s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-27b` | image | ❌ `exception` | 32.23s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-35b-a3b` | image | ❌ `exception` | 19.43s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-397b-a17b` | image | ❌ `timeout` | 59.47s | Timeout limit exceeded |
| `qwen3.5-flash` | image | ❌ `exception` | 23.40s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-omni-flash` | image | ❌ `exception` | 33.66s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-omni-plus` | image | ❌ `exception` | 35.34s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-plus` | image | ❌ `exception` | 27.90s | NoMediaResponseError: No media response from Qwen |
| `qwen3.6-35b-a3b` | image | ❌ `exception` | 27.20s | NoMediaResponseError: No media response from Qwen |
| `qwen3.6-plus` | image | ❌ `exception` | 22.05s | NoMediaResponseError: No media response from Qwen |

## Sample successful responses

### `qwen3.6-plus-preview` — text

```
PONG
```

### `qwen3.6-max-preview` — text

```
PONG
```

### `qwen3.5-max-2026-03-08` — text

```
PONG
```

