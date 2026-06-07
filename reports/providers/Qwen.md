# Qwen

- **Label:** Qwen
- **URL:** https://chat.qwen.ai
- **Models:** 19
- **Working tests:** 3 / 19
- **Avg response time:** 8.18s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `qwen3.5-max-2026-03-08` | text | ✅ `ok` | 10.11s | contains expected token 'PONG' |
| `qwen3.6-max-preview` | text | ✅ `ok` | 7.02s | contains expected token 'PONG' |
| `qwen3.6-plus-preview` | text | ✅ `ok` | 7.43s | contains expected token 'PONG' |
| `qwen-max-latest` | image | ❌ `http_error` | 29.64s | RuntimeError: Response: {'success': False, 'request_id': '93465841-bc15-4418-a13c-229e346bf445', 'data': {'code': 'Not_Found', 'details': 'Model not found'}} |
| `qwen-plus-2025-07-28` | image | ❌ `exception` | 26.00s | NoMediaResponseError: No media response from Qwen |
| `qwen3-coder-plus` | image | ❌ `exception` | 38.65s | NoMediaResponseError: No media response from Qwen |
| `qwen3-max-2026-01-23` | image | ❌ `exception` | 29.40s | NoMediaResponseError: No media response from Qwen |
| `qwen3-omni-flash-2025-12-01` | image | ❌ `exception` | 42.99s | NoMediaResponseError: No media response from Qwen |
| `qwen3-vl-plus` | image | ❌ `timeout` | 46.29s | Timeout limit exceeded |
| `qwen3.5-122b-a10b` | image | ❌ `exception` | 32.16s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-27b` | image | ❌ `exception` | 33.66s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-35b-a3b` | image | ❌ `exception` | 19.61s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-397b-a17b` | image | ❌ `timeout` | 34.21s | Timeout limit exceeded |
| `qwen3.5-flash` | image | ❌ `exception` | 26.34s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-omni-flash` | image | ❌ `exception` | 35.25s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-omni-plus` | image | ❌ `exception` | 23.58s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-plus` | image | ❌ `exception` | 29.68s | NoMediaResponseError: No media response from Qwen |
| `qwen3.6-35b-a3b` | image | ❌ `exception` | 31.56s | NoMediaResponseError: No media response from Qwen |
| `qwen3.6-plus` | image | ❌ `exception` | 33.09s | NoMediaResponseError: No media response from Qwen |

## Sample successful responses

### `qwen3.6-plus-preview` — text

```
PONG
```

### `qwen3.5-max-2026-03-08` — text

```
PONG
```

### `qwen3.6-max-preview` — text

```
PONG
```

