# WeWordle

- **Label:** WeWordle
- **URL:** https://chat-gpt.com
- **Models:** 7
- **Working tests:** 6 / 7
- **Avg response time:** 18.15s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `deepseek` | text | ✅ `ok` | 21.03s | contains expected token 'PONG' |
| `deepseek-r1` | text | ✅ `ok` | 22.03s | contains expected token 'PONG' |
| `deepseek-reasoner` | text | ✅ `ok` | 22.07s | contains expected token 'PONG' |
| `gpt-4` | text | ✅ `ok` | 22.02s | contains expected token 'PONG' |
| `gpt-4o-mini` | text | ✅ `ok` | 1.07s | contains expected token 'PONG' |
| `v3` | text | ✅ `ok` | 20.68s | contains expected token 'PONG' |
| `gpt-4o` | text | ❌ `invalid` | 21.03s | expected 'PONG', got: 'PING' |

## Sample successful responses

### `v3` — text

```
PONG
```

### `gpt-4` — text

```
PONG
```

### `gpt-4o-mini` — text

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

