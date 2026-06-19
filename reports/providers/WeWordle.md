# WeWordle

- **Label:** WeWordle
- **URL:** https://chat-gpt.com
- **Models:** 7
- **Working tests:** 6 / 7
- **Avg response time:** 3.08s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `deepseek` | text | ✅ `ok` | 8.79s | contains expected token 'PONG' |
| `deepseek-r1` | text | ✅ `ok` | 3.07s | contains expected token 'PONG' |
| `deepseek-reasoner` | text | ✅ `ok` | 1.59s | contains expected token 'PONG' |
| `gpt-4` | text | ✅ `ok` | 1.48s | contains expected token 'PONG' |
| `gpt-4o-mini` | text | ✅ `ok` | 2.40s | contains expected token 'PONG' |
| `v3` | text | ✅ `ok` | 1.16s | contains expected token 'PONG' |
| `gpt-4o` | text | ❌ `invalid` | 1.54s | expected 'PONG', got: 'PING' |

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

