# WeWordle

- **Label:** WeWordle
- **URL:** https://chat-gpt.com
- **Models:** 7
- **Working tests:** 5 / 7
- **Avg response time:** 2.04s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `deepseek` | text | ✅ `ok` | 2.71s | contains expected token 'PONG' |
| `deepseek-r1` | text | ✅ `ok` | 1.06s | contains expected token 'PONG' |
| `deepseek-reasoner` | text | ✅ `ok` | 2.46s | contains expected token 'PONG' |
| `gpt-4` | text | ✅ `ok` | 2.12s | contains expected token 'PONG' |
| `v3` | text | ✅ `ok` | 1.84s | contains expected token 'PONG' |
| `gpt-4o` | text | ❌ `invalid` | 1.55s | expected 'PONG', got: 'PING' |
| `gpt-4o-mini` | text | ❌ `invalid` | 1.28s | expected 'PONG', got: 'Game' |

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

