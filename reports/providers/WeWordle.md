# WeWordle

- **Label:** WeWordle
- **URL:** https://chat-gpt.com
- **Models:** 7
- **Working tests:** 6 / 7
- **Avg response time:** 4.20s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `deepseek` | text | ✅ `ok` | 0.77s | contains expected token 'PONG' |
| `deepseek-r1` | text | ✅ `ok` | 15.19s | contains expected token 'PONG' |
| `deepseek-reasoner` | text | ✅ `ok` | 3.40s | contains expected token 'PONG' |
| `gpt-4` | text | ✅ `ok` | 2.09s | contains expected token 'PONG' |
| `gpt-4o-mini` | text | ✅ `ok` | 1.26s | contains expected token 'PONG' |
| `v3` | text | ✅ `ok` | 2.47s | contains expected token 'PONG' |
| `gpt-4o` | text | ❌ `invalid` | 1.16s | expected 'PONG', got: 'PING' |

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

