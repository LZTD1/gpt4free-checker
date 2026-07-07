# WeWordle

- **Label:** WeWordle
- **URL:** https://chat-gpt.com
- **Models:** 7
- **Working tests:** 6 / 7
- **Avg response time:** 1.69s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `deepseek` | text | ✅ `ok` | 1.72s | contains expected token 'PONG' |
| `deepseek-r1` | text | ✅ `ok` | 1.01s | contains expected token 'PONG' |
| `deepseek-reasoner` | text | ✅ `ok` | 1.90s | contains expected token 'PONG' |
| `gpt-4` | text | ✅ `ok` | 1.62s | contains expected token 'PONG' |
| `gpt-4o` | text | ✅ `ok` | 1.15s | contains expected token 'PONG' |
| `v3` | text | ✅ `ok` | 2.75s | contains expected token 'PONG' |
| `gpt-4o-mini` | text | ❌ `invalid` | 1.29s | expected 'PONG', got: 'Game' |

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

