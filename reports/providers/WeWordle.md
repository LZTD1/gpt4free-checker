# WeWordle

- **Label:** WeWordle
- **URL:** https://chat-gpt.com
- **Models:** 7
- **Working tests:** 5 / 7
- **Avg response time:** 2.95s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `deepseek` | text | ✅ `ok` | 1.26s | contains expected token 'PONG' |
| `deepseek-r1` | text | ✅ `ok` | 1.73s | contains expected token 'PONG' |
| `deepseek-reasoner` | text | ✅ `ok` | 3.31s | contains expected token 'PONG' |
| `gpt-4` | text | ✅ `ok` | 3.07s | contains expected token 'PONG' |
| `v3` | text | ✅ `ok` | 5.39s | contains expected token 'PONG' |
| `gpt-4o` | text | ❌ `invalid` | 0.89s | expected 'PONG', got: 'PING' |
| `gpt-4o-mini` | text | ❌ `invalid` | 1.09s | expected 'PONG', got: 'Game' |

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

