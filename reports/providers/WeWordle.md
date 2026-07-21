# WeWordle

- **Label:** WeWordle
- **URL:** https://chat-gpt.com
- **Models:** 7
- **Working tests:** 5 / 7
- **Avg response time:** 17.47s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `deepseek` | text | ✅ `ok` | 21.03s | contains expected token 'PONG' |
| `deepseek-r1` | text | ✅ `ok` | 22.03s | contains expected token 'PONG' |
| `deepseek-reasoner` | text | ✅ `ok` | 21.59s | contains expected token 'PONG' |
| `gpt-4` | text | ✅ `ok` | 0.95s | contains expected token 'PONG' |
| `v3` | text | ✅ `ok` | 21.74s | contains expected token 'PONG' |
| `gpt-4o` | text | ❌ `invalid` | 0.98s | expected 'PONG', got: 'PING' |
| `gpt-4o-mini` | text | ❌ `invalid` | 1.36s | expected 'PONG', got: 'Game' |

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

