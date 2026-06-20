# WeWordle

- **Label:** WeWordle
- **URL:** https://chat-gpt.com
- **Models:** 7
- **Working tests:** 5 / 7
- **Avg response time:** 1.73s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `deepseek` | text | ✅ `ok` | 0.97s | contains expected token 'PONG' |
| `deepseek-r1` | text | ✅ `ok` | 3.84s | contains expected token 'PONG' |
| `deepseek-reasoner` | text | ✅ `ok` | 1.64s | contains expected token 'PONG' |
| `gpt-4` | text | ✅ `ok` | 1.01s | contains expected token 'PONG' |
| `v3` | text | ✅ `ok` | 1.20s | contains expected token 'PONG' |
| `gpt-4o` | text | ❌ `invalid` | 1.10s | expected 'PONG', got: 'PING' |
| `gpt-4o-mini` | text | ❌ `invalid` | 0.98s | expected 'PONG', got: 'PADDLE' |

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

