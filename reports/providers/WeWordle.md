# WeWordle

- **Label:** WeWordle
- **URL:** https://chat-gpt.com
- **Models:** 7
- **Working tests:** 5 / 7
- **Avg response time:** 1.62s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `deepseek` | text | ✅ `ok` | 0.82s | contains expected token 'PONG' |
| `deepseek-r1` | text | ✅ `ok` | 3.00s | contains expected token 'PONG' |
| `deepseek-reasoner` | text | ✅ `ok` | 1.02s | contains expected token 'PONG' |
| `gpt-4` | text | ✅ `ok` | 1.68s | contains expected token 'PONG' |
| `v3` | text | ✅ `ok` | 1.58s | contains expected token 'PONG' |
| `gpt-4o` | text | ❌ `invalid` | 1.25s | expected 'PONG', got: 'PING' |
| `gpt-4o-mini` | text | ❌ `invalid` | 1.06s | expected 'PONG', got: 'Game' |

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

