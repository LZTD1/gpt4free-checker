# WeWordle

- **Label:** WeWordle
- **URL:** https://chat-gpt.com
- **Models:** 7
- **Working tests:** 5 / 7
- **Avg response time:** 2.17s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `deepseek` | text | ✅ `ok` | 2.86s | contains expected token 'PONG' |
| `deepseek-r1` | text | ✅ `ok` | 2.99s | contains expected token 'PONG' |
| `deepseek-reasoner` | text | ✅ `ok` | 1.34s | contains expected token 'PONG' |
| `gpt-4` | text | ✅ `ok` | 1.89s | contains expected token 'PONG' |
| `v3` | text | ✅ `ok` | 1.76s | contains expected token 'PONG' |
| `gpt-4o` | text | ❌ `invalid` | 1.05s | expected 'PONG', got: 'PING' |
| `gpt-4o-mini` | text | ❌ `invalid` | 1.86s | expected 'PONG', got: 'Ping.' |

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

