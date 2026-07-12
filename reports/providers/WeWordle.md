# WeWordle

- **Label:** WeWordle
- **URL:** https://chat-gpt.com
- **Models:** 7
- **Working tests:** 5 / 7
- **Avg response time:** 2.73s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `deepseek` | text | ✅ `ok` | 3.57s | contains expected token 'PONG' |
| `deepseek-r1` | text | ✅ `ok` | 2.36s | contains expected token 'PONG' |
| `deepseek-reasoner` | text | ✅ `ok` | 0.91s | contains expected token 'PONG' |
| `gpt-4` | text | ✅ `ok` | 4.14s | contains expected token 'PONG' |
| `v3` | text | ✅ `ok` | 2.67s | contains expected token 'PONG' |
| `gpt-4o` | text | ❌ `invalid` | 1.62s | expected 'PONG', got: 'PING' |
| `gpt-4o-mini` | text | ❌ `invalid` | 1.13s | expected 'PONG', got: 'Game' |

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

