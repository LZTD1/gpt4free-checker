# WeWordle

- **Label:** WeWordle
- **URL:** https://chat-gpt.com
- **Models:** 7
- **Working tests:** 5 / 7
- **Avg response time:** 1.80s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `deepseek` | text | ✅ `ok` | 3.01s | contains expected token 'PONG' |
| `deepseek-r1` | text | ✅ `ok` | 0.94s | contains expected token 'PONG' |
| `deepseek-reasoner` | text | ✅ `ok` | 1.27s | contains expected token 'PONG' |
| `gpt-4` | text | ✅ `ok` | 1.39s | contains expected token 'PONG' |
| `v3` | text | ✅ `ok` | 2.41s | contains expected token 'PONG' |
| `gpt-4o` | text | ❌ `invalid` | 1.81s | expected 'PONG', got: 'PING' |
| `gpt-4o-mini` | text | ❌ `invalid` | 1.72s | expected 'PONG', got: 'Paddle' |

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

