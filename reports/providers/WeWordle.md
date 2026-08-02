# WeWordle

- **Label:** WeWordle
- **URL:** https://chat-gpt.com
- **Models:** 7
- **Working tests:** 6 / 7
- **Avg response time:** 14.94s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `deepseek` | text | ✅ `ok` | 21.54s | contains expected token 'PONG' |
| `deepseek-r1` | text | ✅ `ok` | 2.26s | contains expected token 'PONG' |
| `deepseek-reasoner` | text | ✅ `ok` | 1.96s | contains expected token 'PONG' |
| `gpt-4` | text | ✅ `ok` | 21.82s | contains expected token 'PONG' |
| `gpt-4o-mini` | text | ✅ `ok` | 21.03s | contains expected token 'PONG' |
| `v3` | text | ✅ `ok` | 21.03s | contains expected token 'PONG' |
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

