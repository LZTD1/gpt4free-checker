# WeWordle

- **Label:** WeWordle
- **URL:** https://chat-gpt.com
- **Models:** 7
- **Working tests:** 6 / 7
- **Avg response time:** 1.82s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `deepseek` | text | ✅ `ok` | 2.38s | contains expected token 'PONG' |
| `deepseek-r1` | text | ✅ `ok` | 2.21s | contains expected token 'PONG' |
| `deepseek-reasoner` | text | ✅ `ok` | 1.05s | contains expected token 'PONG' |
| `gpt-4` | text | ✅ `ok` | 1.37s | contains expected token 'PONG' |
| `gpt-4o-mini` | text | ✅ `ok` | 0.96s | contains expected token 'PONG' |
| `v3` | text | ✅ `ok` | 2.95s | contains expected token 'PONG' |
| `gpt-4o` | text | ❌ `invalid` | 1.17s | expected 'PONG', got: 'PING' |

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

