# WeWordle

- **Label:** WeWordle
- **URL:** https://chat-gpt.com
- **Models:** 7
- **Working tests:** 6 / 7
- **Avg response time:** 2.42s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `deepseek` | text | ✅ `ok` | 1.41s | contains expected token 'PONG' |
| `deepseek-r1` | text | ✅ `ok` | 2.17s | contains expected token 'PONG' |
| `deepseek-reasoner` | text | ✅ `ok` | 2.37s | contains expected token 'PONG' |
| `gpt-4` | text | ✅ `ok` | 2.87s | contains expected token 'PONG' |
| `gpt-4o` | text | ✅ `ok` | 1.70s | contains expected token 'PONG' |
| `v3` | text | ✅ `ok` | 4.00s | contains expected token 'PONG' |
| `gpt-4o-mini` | text | ❌ `invalid` | 1.17s | expected 'PONG', got: 'Game' |

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

