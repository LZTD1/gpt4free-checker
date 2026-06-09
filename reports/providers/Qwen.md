# Qwen

- **Label:** Qwen
- **URL:** https://chat.qwen.ai
- **Models:** 19
- **Working tests:** 3 / 19
- **Avg response time:** 9.08s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `qwen3.5-max-2026-03-08` | text | ✅ `ok` | 13.24s | contains expected token 'PONG' |
| `qwen3.6-max-preview` | text | ✅ `ok` | 8.67s | contains expected token 'PONG' |
| `qwen3.6-plus-preview` | text | ✅ `ok` | 5.32s | contains expected token 'PONG' |
| `qwen-max-latest` | image | ❌ `http_error` | 0.76s | RuntimeError: Response: {'success': False, 'request_id': '337dce9b-ae0f-44c1-ba0b-2bf0bf19a811', 'data': {'code': 'Not_Found', 'details': 'Model not found'}} |
| `qwen-plus-2025-07-28` | image | ❌ `exception` | 14.91s | NoMediaResponseError: No media response from Qwen |
| `qwen3-coder-plus` | image | ❌ `exception` | 17.25s | NoMediaResponseError: No media response from Qwen |
| `qwen3-max-2026-01-23` | image | ❌ `exception` | 8.08s | NoMediaResponseError: No media response from Qwen |
| `qwen3-omni-flash-2025-12-01` | image | ❌ `exception` | 27.97s | NoMediaResponseError: No media response from Qwen |
| `qwen3-vl-plus` | image | ❌ `exception` | 26.60s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-122b-a10b` | image | ❌ `exception` | 10.04s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-27b` | image | ❌ `exception` | 5.30s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-35b-a3b` | image | ❌ `exception` | 5.65s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-397b-a17b` | image | ❌ `exception` | 21.88s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-flash` | image | ❌ `exception` | 5.70s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-omni-flash` | image | ❌ `exception` | 19.39s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-omni-plus` | image | ❌ `exception` | 14.11s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-plus` | image | ❌ `exception` | 11.53s | NoMediaResponseError: No media response from Qwen |
| `qwen3.6-35b-a3b` | image | ❌ `exception` | 14.23s | NoMediaResponseError: No media response from Qwen |
| `qwen3.6-plus` | image | ❌ `exception` | 12.31s | NoMediaResponseError: No media response from Qwen |

## Sample successful responses

### `qwen3.6-max-preview` — text

```
PONG
```

### `qwen3.5-max-2026-03-08` — text

```
PONG
```

### `qwen3.6-plus-preview` — text

```
PONG
```

