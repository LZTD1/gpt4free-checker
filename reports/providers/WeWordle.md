# WeWordle

- **Label:** WeWordle
- **URL:** https://chat-gpt.com
- **Models:** 7
- **Working tests:** 5 / 7
- **Avg response time:** 2.41s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `deepseek` | text | ✅ `ok` | 3.04s | contains expected token 'PONG' |
| `deepseek-r1` | text | ✅ `ok` | 3.05s | contains expected token 'PONG' |
| `deepseek-reasoner` | text | ✅ `ok` | 1.69s | contains expected token 'PONG' |
| `gpt-4` | text | ✅ `ok` | 2.26s | contains expected token 'PONG' |
| `v3` | text | ✅ `ok` | 2.01s | contains expected token 'PONG' |
| `gpt-4o` | text | ❌ `invalid` | 1.17s | expected 'PONG', got: 'PING' |
| `gpt-4o-mini` | text | ❌ `invalid` | 0.92s | expected 'PONG', got: 'GAME' |

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

