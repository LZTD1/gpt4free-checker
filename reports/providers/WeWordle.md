# WeWordle

- **Label:** WeWordle
- **URL:** https://chat-gpt.com
- **Models:** 7
- **Working tests:** 5 / 7
- **Avg response time:** 4.82s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `deepseek` | text | ✅ `ok` | 3.18s | contains expected token 'PONG' |
| `deepseek-r1` | text | ✅ `ok` | 12.49s | contains expected token 'PONG' |
| `deepseek-reasoner` | text | ✅ `ok` | 2.64s | contains expected token 'PONG' |
| `gpt-4` | text | ✅ `ok` | 3.96s | contains expected token 'PONG' |
| `v3` | text | ✅ `ok` | 1.83s | contains expected token 'PONG' |
| `gpt-4o` | text | ❌ `invalid` | 1.90s | expected 'PONG', got: 'PING' |
| `gpt-4o-mini` | text | ❌ `invalid` | 1.22s | expected 'PONG', got: 'Game' |

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

