# WeWordle

- **Label:** WeWordle
- **URL:** https://chat-gpt.com
- **Models:** 7
- **Working tests:** 5 / 7
- **Avg response time:** 21.65s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `deepseek` | text | ✅ `ok` | 21.03s | contains expected token 'PONG' |
| `deepseek-r1` | text | ✅ `ok` | 1.89s | contains expected token 'PONG' |
| `deepseek-reasoner` | text | ✅ `ok` | 42.32s | contains expected token 'PONG' |
| `gpt-4` | text | ✅ `ok` | 21.98s | contains expected token 'PONG' |
| `v3` | text | ✅ `ok` | 21.03s | contains expected token 'PONG' |
| `gpt-4o` | text | ❌ `invalid` | 21.03s | expected 'PONG', got: 'PING' |
| `gpt-4o-mini` | text | ❌ `invalid` | 2.26s | expected 'PONG', got: 'PING' |

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

