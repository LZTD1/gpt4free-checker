# WeWordle

- **Label:** WeWordle
- **URL:** https://chat-gpt.com
- **Models:** 7
- **Working tests:** 5 / 7
- **Avg response time:** 3.29s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `deepseek` | text | ✅ `ok` | 2.94s | contains expected token 'PONG' |
| `deepseek-r1` | text | ✅ `ok` | 2.27s | contains expected token 'PONG' |
| `deepseek-reasoner` | text | ✅ `ok` | 6.35s | contains expected token 'PONG' |
| `gpt-4` | text | ✅ `ok` | 2.79s | contains expected token 'PONG' |
| `v3` | text | ✅ `ok` | 2.10s | contains expected token 'PONG' |
| `gpt-4o` | text | ❌ `invalid` | 1.24s | expected 'PONG', got: 'PING' |
| `gpt-4o-mini` | text | ❌ `invalid` | 1.24s | expected 'PONG', got: 'Game' |

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

