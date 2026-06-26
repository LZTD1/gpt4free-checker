# Qwen

- **Label:** Qwen
- **URL:** https://chat.qwen.ai
- **Models:** 23
- **Working tests:** 5 / 23
- **Avg response time:** 6.82s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `qwen-latest-series-invite-beta-v16` | text | ✅ `ok` | 3.76s | contains expected token 'PONG' |
| `qwen-latest-series-invite-beta-v24` | text | ✅ `ok` | 5.89s | contains expected token 'PONG' |
| `qwen3.5-max-2026-03-08` | text | ✅ `ok` | 10.05s | contains expected token 'PONG' |
| `qwen3.6-max-preview` | text | ✅ `ok` | 5.68s | contains expected token 'PONG' |
| `qwen3.6-plus-preview` | text | ✅ `ok` | 8.71s | contains expected token 'PONG' |
| `qwen-plus-2025-07-28` | image | ❌ `exception` | 15.98s | NoMediaResponseError: No media response from Qwen |
| `qwen3-coder-plus` | image | ❌ `exception` | 16.99s | NoMediaResponseError: No media response from Qwen |
| `qwen3-max-2026-01-23` | image | ❌ `exception` | 8.28s | NoMediaResponseError: No media response from Qwen |
| `qwen3-omni-flash-2025-12-01` | image | ❌ `exception` | 1.02s | ResponseError: quota_limit: The service is currently experiencing high demand. Please try again later. |
| `qwen3-vl-plus` | image | ❌ `timeout` | 91.47s | Timeout limit exceeded |
| `qwen3.5-122b-a10b` | image | ❌ `exception` | 7.20s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-27b` | image | ❌ `exception` | 12.82s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-35b-a3b` | image | ❌ `exception` | 7.02s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-397b-a17b` | image | ❌ `exception` | 27.47s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-flash` | image | ❌ `exception` | 9.03s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-omni-flash` | image | ❌ `exception` | 14.83s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-omni-plus` | image | ❌ `exception` | 19.99s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-plus` | image | ❌ `exception` | 11.39s | NoMediaResponseError: No media response from Qwen |
| `qwen3.6-27b` | image | ❌ `exception` | 13.36s | NoMediaResponseError: No media response from Qwen |
| `qwen3.6-35b-a3b` | image | ❌ `exception` | 9.01s | NoMediaResponseError: No media response from Qwen |
| `qwen3.6-plus` | image | ❌ `exception` | 11.59s | NoMediaResponseError: No media response from Qwen |
| `qwen3.7-max` | image | ❌ `exception` | 10.26s | NoMediaResponseError: No media response from Qwen |
| `qwen3.7-plus` | image | ❌ `exception` | 19.43s | NoMediaResponseError: No media response from Qwen |

## Sample successful responses

### `qwen3.6-max-preview` — text

```
PONG
```

### `qwen-latest-series-invite-beta-v24` — text

```
PONG
```

### `qwen-latest-series-invite-beta-v16` — text

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

