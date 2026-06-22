# WeWordle

- **Label:** WeWordle
- **URL:** https://chat-gpt.com
- **Models:** 7
- **Working tests:** 5 / 7
- **Avg response time:** 2.50s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `deepseek` | text | ✅ `ok` | 2.99s | contains expected token 'PONG' |
| `deepseek-r1` | text | ✅ `ok` | 2.44s | contains expected token 'PONG' |
| `deepseek-reasoner` | text | ✅ `ok` | 1.50s | contains expected token 'PONG' |
| `gpt-4` | text | ✅ `ok` | 2.33s | contains expected token 'PONG' |
| `v3` | text | ✅ `ok` | 3.21s | contains expected token 'PONG' |
| `gpt-4o` | text | ❌ `invalid` | 1.20s | expected 'PONG', got: 'PING' |
| `gpt-4o-mini` | text | ❌ `invalid` | 0.99s | expected 'PONG', got: 'Play.' |

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

