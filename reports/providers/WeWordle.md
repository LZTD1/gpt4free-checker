# WeWordle

- **Label:** WeWordle
- **URL:** https://chat-gpt.com
- **Models:** 7
- **Working tests:** 5 / 7
- **Avg response time:** 4.03s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `deepseek` | text | ✅ `ok` | 2.88s | contains expected token 'PONG' |
| `deepseek-r1` | text | ✅ `ok` | 10.69s | contains expected token 'PONG' |
| `deepseek-reasoner` | text | ✅ `ok` | 2.51s | contains expected token 'PONG' |
| `gpt-4` | text | ✅ `ok` | 2.15s | contains expected token 'PONG' |
| `v3` | text | ✅ `ok` | 1.94s | contains expected token 'PONG' |
| `gpt-4o` | text | ❌ `invalid` | 1.49s | expected 'PONG', got: 'PING' |
| `gpt-4o-mini` | text | ❌ `invalid` | 1.47s | expected 'PONG', got: 'Game' |

## Sample successful responses

### `v3` — text

```
PONG
```

### `gpt-4` — text

```
PONGPONG
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

