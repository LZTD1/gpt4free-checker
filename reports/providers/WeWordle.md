# WeWordle

- **Label:** WeWordle
- **URL:** https://chat-gpt.com
- **Models:** 7
- **Working tests:** 5 / 7
- **Avg response time:** 13.13s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `deepseek` | text | ✅ `ok` | 1.72s | contains expected token 'PONG' |
| `deepseek-r1` | text | ✅ `ok` | 20.42s | contains expected token 'PONG' |
| `deepseek-reasoner` | text | ✅ `ok` | 21.03s | contains expected token 'PONG' |
| `gpt-4` | text | ✅ `ok` | 1.68s | contains expected token 'PONG' |
| `v3` | text | ✅ `ok` | 20.80s | contains expected token 'PONG' |
| `gpt-4o` | text | ❌ `invalid` | 1.05s | expected 'PONG', got: 'PING' |
| `gpt-4o-mini` | text | ❌ `invalid` | 41.09s | expected 'PONG', got: 'PING' |

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

