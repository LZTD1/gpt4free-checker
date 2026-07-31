# WeWordle

- **Label:** WeWordle
- **URL:** https://chat-gpt.com
- **Models:** 7
- **Working tests:** 5 / 7
- **Avg response time:** 29.67s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `deepseek` | text | ✅ `ok` | 22.03s | contains expected token 'PONG' |
| `deepseek-r1` | text | ✅ `ok` | 42.42s | contains expected token 'PONG' |
| `deepseek-reasoner` | text | ✅ `ok` | 41.61s | contains expected token 'PONG' |
| `gpt-4` | text | ✅ `ok` | 20.68s | contains expected token 'PONG' |
| `v3` | text | ✅ `ok` | 21.59s | contains expected token 'PONG' |
| `gpt-4o` | text | ❌ `invalid` | 1.65s | expected 'PONG', got: 'PING' |
| `gpt-4o-mini` | text | ❌ `invalid` | 21.64s | expected 'PONG', got: 'Game' |

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

