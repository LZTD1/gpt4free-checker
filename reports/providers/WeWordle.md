# WeWordle

- **Label:** WeWordle
- **URL:** https://chat-gpt.com
- **Models:** 7
- **Working tests:** 5 / 7
- **Avg response time:** 25.88s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `deepseek` | text | ✅ `ok` | 42.33s | contains expected token 'PONG' |
| `deepseek-r1` | text | ✅ `ok` | 21.69s | contains expected token 'PONG' |
| `deepseek-reasoner` | text | ✅ `ok` | 1.99s | contains expected token 'PONG' |
| `gpt-4` | text | ✅ `ok` | 41.36s | contains expected token 'PONG' |
| `v3` | text | ✅ `ok` | 22.02s | contains expected token 'PONG' |
| `gpt-4o` | text | ❌ `invalid` | 1.24s | expected 'PONG', got: 'PING' |
| `gpt-4o-mini` | text | ❌ `invalid` | 21.02s | expected 'PONG', got: 'Game' |

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

