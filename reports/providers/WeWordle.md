# WeWordle

- **Label:** WeWordle
- **URL:** https://chat-gpt.com
- **Models:** 7
- **Working tests:** 5 / 7
- **Avg response time:** 3.12s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `deepseek` | text | ✅ `ok` | 1.79s | contains expected token 'PONG' |
| `deepseek-r1` | text | ✅ `ok` | 2.71s | contains expected token 'PONG' |
| `deepseek-reasoner` | text | ✅ `ok` | 4.06s | contains expected token 'PONG' |
| `gpt-4` | text | ✅ `ok` | 2.10s | contains expected token 'PONG' |
| `v3` | text | ✅ `ok` | 4.96s | contains expected token 'PONG' |
| `gpt-4o` | text | ❌ `invalid` | 1.15s | expected 'PONG', got: 'PING' |
| `gpt-4o-mini` | text | ❌ `invalid` | 1.54s | expected 'PONG', got: 'Game' |

## Sample successful responses

### `v3` — text

```
PONG
```

### `gpt-4` — text

```
PONG
```

### `deepseek` — text

```
PONG
```

### `deepseek-reasoner` — text

```
PONG
```

### `deepseek-r1` — text

```
PONG
```

