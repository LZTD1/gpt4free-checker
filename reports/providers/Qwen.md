# Qwen

- **Label:** Qwen
- **URL:** https://chat.qwen.ai
- **Models:** 19
- **Working tests:** 3 / 19
- **Avg response time:** 7.59s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `qwen3.5-max-2026-03-08` | text | ✅ `ok` | 10.54s | contains expected token 'PONG' |
| `qwen3.6-max-preview` | text | ✅ `ok` | 7.15s | contains expected token 'PONG' |
| `qwen3.6-plus-preview` | text | ✅ `ok` | 5.08s | contains expected token 'PONG' |
| `qwen-max-latest` | image | ❌ `http_error` | 20.08s | RuntimeError: Response: {'success': False, 'request_id': '3f6ecfd8-1a84-4cab-9d2b-02f0e13b48ee', 'data': {'code': 'Not_Found', 'details': 'Model not found'}} |
| `qwen-plus-2025-07-28` | image | ❌ `exception` | 31.45s | NoMediaResponseError: No media response from Qwen |
| `qwen3-coder-plus` | image | ❌ `exception` | 29.50s | NoMediaResponseError: No media response from Qwen |
| `qwen3-max-2026-01-23` | image | ❌ `exception` | 26.31s | NoMediaResponseError: No media response from Qwen |
| `qwen3-omni-flash-2025-12-01` | image | ❌ `exception` | 22.78s | NoMediaResponseError: No media response from Qwen |
| `qwen3-vl-plus` | image | ❌ `timeout` | 82.72s | Timeout limit exceeded |
| `qwen3.5-122b-a10b` | image | ❌ `exception` | 27.99s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-27b` | image | ❌ `exception` | 24.20s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-35b-a3b` | image | ❌ `exception` | 26.62s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-397b-a17b` | image | ❌ `exception` | 42.30s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-flash` | image | ❌ `exception` | 19.27s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-omni-flash` | image | ❌ `timeout` | 42.58s | Timeout limit exceeded |
| `qwen3.5-omni-plus` | image | ❌ `exception` | 20.67s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-plus` | image | ❌ `exception` | 32.20s | NoMediaResponseError: No media response from Qwen |
| `qwen3.6-35b-a3b` | image | ❌ `timeout` | 91.84s | Timeout limit exceeded |
| `qwen3.6-plus` | image | ❌ `exception` | 25.83s | NoMediaResponseError: No media response from Qwen |

## Sample successful responses

### `qwen3.6-max-preview` — text

```
PONG
```

### `qwen3.6-plus-preview` — text

```
PONG
```

### `qwen3.5-max-2026-03-08` — text

```
PONG
```

