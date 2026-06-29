# Qwen

- **Label:** Qwen
- **URL:** https://chat.qwen.ai
- **Models:** 23
- **Working tests:** 5 / 23
- **Avg response time:** 10.25s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `qwen-latest-series-invite-beta-v16` | text | ✅ `ok` | 6.42s | contains expected token 'PONG' |
| `qwen-latest-series-invite-beta-v24` | text | ✅ `ok` | 18.18s | contains expected token 'PONG' |
| `qwen3.5-max-2026-03-08` | text | ✅ `ok` | 13.16s | contains expected token 'PONG' |
| `qwen3.6-max-preview` | text | ✅ `ok` | 5.93s | contains expected token 'PONG' |
| `qwen3.6-plus-preview` | text | ✅ `ok` | 7.55s | contains expected token 'PONG' |
| `qwen-plus-2025-07-28` | image | ❌ `exception` | 14.81s | NoMediaResponseError: No media response from Qwen |
| `qwen3-coder-plus` | image | ❌ `exception` | 41.12s | NoMediaResponseError: No media response from Qwen |
| `qwen3-max-2026-01-23` | image | ❌ `exception` | 8.16s | NoMediaResponseError: No media response from Qwen |
| `qwen3-omni-flash-2025-12-01` | image | ❌ `exception` | 28.26s | NoMediaResponseError: No media response from Qwen |
| `qwen3-vl-plus` | image | ❌ `timeout` | 81.83s | Timeout limit exceeded |
| `qwen3.5-122b-a10b` | image | ❌ `exception` | 14.99s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-27b` | image | ❌ `exception` | 12.10s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-35b-a3b` | image | ❌ `exception` | 6.62s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-397b-a17b` | image | ❌ `exception` | 20.69s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-flash` | image | ❌ `exception` | 5.35s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-omni-flash` | image | ❌ `exception` | 14.18s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-omni-plus` | image | ❌ `exception` | 18.00s | NoMediaResponseError: No media response from Qwen |
| `qwen3.5-plus` | image | ❌ `exception` | 10.48s | NoMediaResponseError: No media response from Qwen |
| `qwen3.6-27b` | image | ❌ `exception` | 25.79s | NoMediaResponseError: No media response from Qwen |
| `qwen3.6-35b-a3b` | image | ❌ `exception` | 11.44s | NoMediaResponseError: No media response from Qwen |
| `qwen3.6-plus` | image | ❌ `exception` | 12.29s | NoMediaResponseError: No media response from Qwen |
| `qwen3.7-max` | image | ❌ `exception` | 10.12s | NoMediaResponseError: No media response from Qwen |
| `qwen3.7-plus` | image | ❌ `exception` | 13.91s | NoMediaResponseError: No media response from Qwen |

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

