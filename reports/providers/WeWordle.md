# WeWordle

- **Label:** WeWordle
- **URL:** https://chat-gpt.com
- **Models:** 7
- **Working tests:** 6 / 7
- **Avg response time:** 4.14s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `deepseek` | text | ✅ `ok` | 2.07s | contains expected token 'PONG' |
| `deepseek-r1` | text | ✅ `ok` | 2.61s | contains expected token 'PONG' |
| `deepseek-reasoner` | text | ✅ `ok` | 12.71s | contains expected token 'PONG' |
| `gpt-4` | text | ✅ `ok` | 2.50s | contains expected token 'PONG' |
| `gpt-4o` | text | ✅ `ok` | 1.68s | contains expected token 'PONG' |
| `v3` | text | ✅ `ok` | 3.26s | contains expected token 'PONG' |
| `gpt-4o-mini` | text | ❌ `invalid` | 1.42s | expected 'PONG', got: 'Game' |

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

