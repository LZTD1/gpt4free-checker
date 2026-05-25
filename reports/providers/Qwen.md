# Qwen

- **Label:** Qwen
- **URL:** https://chat.qwen.ai
- **Models:** 19
- **Working tests:** 3 / 19
- **Avg response time:** 15.24s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `qwen3.5-max-2026-03-08` | text | ✅ `ok` | 17.89s | contains expected token 'PONG' |
| `qwen3.6-max-preview` | text | ✅ `ok` | 10.89s | contains expected token 'PONG' |
| `qwen3.6-plus-preview` | text | ✅ `ok` | 16.95s | contains expected token 'PONG' |
| `qwen-max-latest` | image | ❌ `exception` | 65.89s | NoMediaResponseError: No media response from Qwen |
| `qwen-plus-2025-07-28` | image | ❌ `exception` | 63.95s | NoMediaResponseError: No media response from Qwen |
| `qwen3-coder-plus` | image | ❌ `exception` | 13.79s | NoMediaResponseError: No media response from Qwen |
| `qwen3-max-2026-01-23` | image | ❌ `exception` | 60.55s | NoMediaResponseError: No media response from Qwen |
| `qwen3-omni-flash-2025-12-01` | image | ❌ `timeout` | 79.27s | Timeout limit exceeded |
| `qwen3-vl-plus` | image | ❌ `timeout` | 109.41s | Timeout limit exceeded |
| `qwen3.5-122b-a10b` | image | ❌ `exception` | 56.89s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-27b` | image | ❌ `exception` | 20.04s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-35b-a3b` | image | ❌ `exception` | 45.33s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-397b-a17b` | image | ❌ `timeout` | 79.13s | Timeout limit exceeded |
| `qwen3.5-flash` | image | ❌ `timeout` | 4444.76s | Timeout limit exceeded |
| `qwen3.5-omni-flash` | image | ❌ `exception` | 58.22s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-omni-plus` | image | ❌ `exception` | 40.95s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-plus` | image | ❌ `exception` | 51.25s | NoMediaResponseError: No media response from Qwen |
| `qwen3.6-35b-a3b` | image | ❌ `timeout` | 78.73s | Timeout limit exceeded |
| `qwen3.6-plus` | image | ❌ `exception` | 58.20s | NoMediaResponseError: No media response from Qwen |

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

