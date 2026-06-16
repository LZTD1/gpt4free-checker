# WeWordle

- **Label:** WeWordle
- **URL:** https://chat-gpt.com
- **Models:** 7
- **Working tests:** 5 / 7
- **Avg response time:** 2.27s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `deepseek` | text | ✅ `ok` | 0.81s | contains expected token 'PONG' |
| `deepseek-r1` | text | ✅ `ok` | 1.81s | contains expected token 'PONG' |
| `deepseek-reasoner` | text | ✅ `ok` | 5.39s | contains expected token 'PONG' |
| `gpt-4` | text | ✅ `ok` | 1.72s | contains expected token 'PONG' |
| `v3` | text | ✅ `ok` | 1.63s | contains expected token 'PONG' |
| `gpt-4o` | text | ❌ `invalid` | 2.22s | expected 'PONG', got: 'PING' |
| `gpt-4o-mini` | text | ❌ `invalid` | 1.19s | expected 'PONG', got: 'Game' |

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

