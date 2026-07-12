# WeWordle

- **Label:** WeWordle
- **URL:** https://chat-gpt.com
- **Models:** 7
- **Working tests:** 5 / 7
- **Avg response time:** 2.13s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `deepseek` | text | ✅ `ok` | 2.52s | contains expected token 'PONG' |
| `deepseek-r1` | text | ✅ `ok` | 1.91s | contains expected token 'PONG' |
| `deepseek-reasoner` | text | ✅ `ok` | 1.53s | contains expected token 'PONG' |
| `gpt-4` | text | ✅ `ok` | 1.97s | contains expected token 'PONG' |
| `v3` | text | ✅ `ok` | 2.70s | contains expected token 'PONG' |
| `gpt-4o` | text | ❌ `invalid` | 1.32s | expected 'PONG', got: 'PING' |
| `gpt-4o-mini` | text | ❌ `invalid` | 1.36s | expected 'PONG', got: 'Game' |

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

