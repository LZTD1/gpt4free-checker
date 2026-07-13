# WeWordle

- **Label:** WeWordle
- **URL:** https://chat-gpt.com
- **Models:** 7
- **Working tests:** 6 / 7
- **Avg response time:** 3.90s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `deepseek` | text | ✅ `ok` | 3.11s | contains expected token 'PONG' |
| `deepseek-r1` | text | ✅ `ok` | 12.73s | contains expected token 'PONG' |
| `deepseek-reasoner` | text | ✅ `ok` | 1.49s | contains expected token 'PONG' |
| `gpt-4` | text | ✅ `ok` | 3.36s | contains expected token 'PONG' |
| `gpt-4o` | text | ✅ `ok` | 1.28s | contains expected token 'PONG' |
| `v3` | text | ✅ `ok` | 1.46s | contains expected token 'PONG' |
| `gpt-4o-mini` | text | ❌ `invalid` | 1.24s | expected 'PONG', got: 'Game' |

## Sample successful responses

### `v3` — text

```
PONG
```

### `gpt-4` — text

```
PONG
```

### `gpt-4o` — text

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

