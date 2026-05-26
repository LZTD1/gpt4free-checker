# Qwen

- **Label:** Qwen
- **URL:** https://chat.qwen.ai
- **Models:** 19
- **Working tests:** 3 / 19
- **Avg response time:** 13.71s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `qwen3.5-max-2026-03-08` | text | ✅ `ok` | 8.70s | contains expected token 'PONG' |
| `qwen3.6-max-preview` | text | ✅ `ok` | 8.66s | contains expected token 'PONG' |
| `qwen3.6-plus-preview` | text | ✅ `ok` | 23.78s | contains expected token 'PONG' |
| `qwen-max-latest` | image | ❌ `timeout` | 62.15s | Timeout limit exceeded |
| `qwen-plus-2025-07-28` | image | ❌ `exception` | 41.44s | NoMediaResponseError: No media response from Qwen |
| `qwen3-coder-plus` | image | ❌ `exception` | 32.48s | NoMediaResponseError: No media response from Qwen |
| `qwen3-max-2026-01-23` | image | ❌ `exception` | 24.25s | NoMediaResponseError: No media response from Qwen |
| `qwen3-omni-flash-2025-12-01` | image | ❌ `exception` | 37.60s | NoMediaResponseError: No media response from Qwen |
| `qwen3-vl-plus` | image | ❌ `timeout` | 56.17s | Timeout limit exceeded |
| `qwen3.5-122b-a10b` | image | ❌ `exception` | 43.93s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-27b` | image | ❌ `timeout` | 76.63s | Timeout limit exceeded |
| `qwen3.5-35b-a3b` | image | ❌ `exception` | 21.44s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-397b-a17b` | image | ❌ `timeout` | 52.43s | Timeout limit exceeded |
| `qwen3.5-flash` | image | ❌ `exception` | 18.06s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-omni-flash` | image | ❌ `timeout` | 138.37s | Timeout limit exceeded |
| `qwen3.5-omni-plus` | image | ❌ `exception` | 41.53s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-plus` | image | ❌ `exception` | 37.17s | NoMediaResponseError: No media response from Qwen |
| `qwen3.6-35b-a3b` | image | ❌ `exception` | 44.32s | NoMediaResponseError: No media response from Qwen |
| `qwen3.6-plus` | image | ❌ `exception` | 30.43s | NoMediaResponseError: No media response from Qwen |

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

