# WeWordle

- **Label:** WeWordle
- **URL:** https://chat-gpt.com
- **Models:** 7
- **Working tests:** 5 / 7
- **Avg response time:** 2.23s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `deepseek` | text | ✅ `ok` | 1.81s | contains expected token 'PONG' |
| `deepseek-r1` | text | ✅ `ok` | 2.48s | contains expected token 'PONG' |
| `deepseek-reasoner` | text | ✅ `ok` | 2.36s | contains expected token 'PONG' |
| `gpt-4` | text | ✅ `ok` | 2.00s | contains expected token 'PONG' |
| `v3` | text | ✅ `ok` | 2.50s | contains expected token 'PONG' |
| `gpt-4o` | text | ❌ `invalid` | 1.94s | expected 'PONG', got: 'PING' |
| `gpt-4o-mini` | text | ❌ `invalid` | 1.52s | expected 'PONG', got: 'Game' |

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

