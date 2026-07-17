# WeWordle

- **Label:** WeWordle
- **URL:** https://chat-gpt.com
- **Models:** 7
- **Working tests:** 6 / 7
- **Avg response time:** 2.54s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `deepseek` | text | ✅ `ok` | 3.04s | contains expected token 'PONG' |
| `deepseek-r1` | text | ✅ `ok` | 1.83s | contains expected token 'PONG' |
| `deepseek-reasoner` | text | ✅ `ok` | 3.64s | contains expected token 'PONG' |
| `gpt-4` | text | ✅ `ok` | 3.11s | contains expected token 'PONG' |
| `gpt-4o-mini` | text | ✅ `ok` | 1.15s | contains expected token 'PONG' |
| `v3` | text | ✅ `ok` | 2.49s | contains expected token 'PONG' |
| `gpt-4o` | text | ❌ `invalid` | 1.05s | expected 'PONG', got: 'PING' |

## Sample successful responses

### `v3` — text

```
PONG
```

### `gpt-4` — text

```
PONGPONG
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

