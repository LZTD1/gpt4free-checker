# WeWordle

- **Label:** WeWordle
- **URL:** https://chat-gpt.com
- **Models:** 7
- **Working tests:** 6 / 7
- **Avg response time:** 21.43s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `deepseek` | text | ✅ `ok` | 22.03s | contains expected token 'PONG' |
| `deepseek-r1` | text | ✅ `ok` | 1.36s | contains expected token 'PONG' |
| `deepseek-reasoner` | text | ✅ `ok` | 21.03s | contains expected token 'PONG' |
| `gpt-4` | text | ✅ `ok` | 41.12s | contains expected token 'PONG' |
| `gpt-4o` | text | ✅ `ok` | 21.03s | contains expected token 'PONG' |
| `v3` | text | ✅ `ok` | 22.03s | contains expected token 'PONG' |
| `gpt-4o-mini` | text | ❌ `invalid` | 21.77s | expected 'PONG', got: 'Game' |

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

