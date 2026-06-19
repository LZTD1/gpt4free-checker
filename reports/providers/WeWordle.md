# WeWordle

- **Label:** WeWordle
- **URL:** https://chat-gpt.com
- **Models:** 7
- **Working tests:** 5 / 7
- **Avg response time:** 2.17s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `deepseek` | text | ✅ `ok` | 2.64s | contains expected token 'PONG' |
| `deepseek-r1` | text | ✅ `ok` | 1.54s | contains expected token 'PONG' |
| `deepseek-reasoner` | text | ✅ `ok` | 3.08s | contains expected token 'PONG' |
| `gpt-4` | text | ✅ `ok` | 2.04s | contains expected token 'PONG' |
| `v3` | text | ✅ `ok` | 1.55s | contains expected token 'PONG' |
| `gpt-4o` | text | ❌ `invalid` | 1.64s | expected 'PONG', got: 'PING' |
| `gpt-4o-mini` | text | ❌ `invalid` | 1.76s | expected 'PONG', got: 'Game' |

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

