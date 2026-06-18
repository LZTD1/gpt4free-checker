# WeWordle

- **Label:** WeWordle
- **URL:** https://chat-gpt.com
- **Models:** 7
- **Working tests:** 6 / 7
- **Avg response time:** 3.97s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `deepseek` | text | ✅ `ok` | 1.03s | contains expected token 'PONG' |
| `deepseek-r1` | text | ✅ `ok` | 0.82s | contains expected token 'PONG' |
| `deepseek-reasoner` | text | ✅ `ok` | 17.69s | contains expected token 'PONG' |
| `gpt-4` | text | ✅ `ok` | 1.40s | contains expected token 'PONG' |
| `gpt-4o-mini` | text | ✅ `ok` | 1.44s | contains expected token 'PONG' |
| `v3` | text | ✅ `ok` | 1.43s | contains expected token 'PONG' |
| `gpt-4o` | text | ❌ `invalid` | 1.21s | expected 'PONG', got: 'PING' |

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

