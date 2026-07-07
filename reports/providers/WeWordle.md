# WeWordle

- **Label:** WeWordle
- **URL:** https://chat-gpt.com
- **Models:** 7
- **Working tests:** 6 / 7
- **Avg response time:** 2.61s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `deepseek` | text | ✅ `ok` | 3.40s | contains expected token 'PONG' |
| `deepseek-r1` | text | ✅ `ok` | 3.51s | contains expected token 'PONG' |
| `deepseek-reasoner` | text | ✅ `ok` | 1.83s | contains expected token 'PONG' |
| `gpt-4` | text | ✅ `ok` | 1.78s | contains expected token 'PONG' |
| `gpt-4o` | text | ✅ `ok` | 1.28s | contains expected token 'PONG' |
| `v3` | text | ✅ `ok` | 3.86s | contains expected token 'PONG' |
| `gpt-4o-mini` | text | ❌ `invalid` | 0.91s | expected 'PONG', got: 'Game' |

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

