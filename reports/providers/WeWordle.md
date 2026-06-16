# WeWordle

- **Label:** WeWordle
- **URL:** https://chat-gpt.com
- **Models:** 7
- **Working tests:** 6 / 7
- **Avg response time:** 2.86s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `deepseek` | text | ✅ `ok` | 1.15s | contains expected token 'PONG' |
| `deepseek-r1` | text | ✅ `ok` | 9.30s | contains expected token 'PONG' |
| `deepseek-reasoner` | text | ✅ `ok` | 1.19s | contains expected token 'PONG' |
| `gpt-4` | text | ✅ `ok` | 2.09s | contains expected token 'PONG' |
| `gpt-4o` | text | ✅ `ok` | 2.18s | contains expected token 'PONG' |
| `v3` | text | ✅ `ok` | 1.22s | contains expected token 'PONG' |
| `gpt-4o-mini` | text | ❌ `invalid` | 1.30s | expected 'PONG', got: 'Ping' |

## Sample successful responses

### `v3` — text

```
PONG
```

### `gpt-4` — text

```
PONG
```

### `gpt-4o` — text

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

