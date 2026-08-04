# WeWordle

- **Label:** WeWordle
- **URL:** https://chat-gpt.com
- **Models:** 7
- **Working tests:** 5 / 7
- **Avg response time:** 9.07s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `deepseek` | text | ✅ `ok` | 0.73s | contains expected token 'PONG' |
| `deepseek-r1` | text | ✅ `ok` | 1.48s | contains expected token 'PONG' |
| `deepseek-reasoner` | text | ✅ `ok` | 1.62s | contains expected token 'PONG' |
| `gpt-4` | text | ✅ `ok` | 20.48s | contains expected token 'PONG' |
| `v3` | text | ✅ `ok` | 21.02s | contains expected token 'PONG' |
| `gpt-4o` | text | ❌ `invalid` | 21.02s | expected 'PONG', got: 'PING' |
| `gpt-4o-mini` | text | ❌ `invalid` | 0.91s | expected 'PONG', got: 'Game' |

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

