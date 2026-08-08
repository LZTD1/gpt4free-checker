# WeWordle

- **Label:** WeWordle
- **URL:** https://chat-gpt.com
- **Models:** 7
- **Working tests:** 5 / 7
- **Avg response time:** 17.33s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `deepseek` | text | ✅ `ok` | 21.03s | contains expected token 'PONG' |
| `deepseek-r1` | text | ✅ `ok` | 21.03s | contains expected token 'PONG' |
| `deepseek-reasoner` | text | ✅ `ok` | 1.24s | contains expected token 'PONG' |
| `gpt-4` | text | ✅ `ok` | 22.03s | contains expected token 'PONG' |
| `v3` | text | ✅ `ok` | 21.35s | contains expected token 'PONG' |
| `gpt-4o` | text | ❌ `invalid` | 21.03s | expected 'PONG', got: 'PING' |
| `gpt-4o-mini` | text | ❌ `invalid` | 1.53s | expected 'PONG', got: 'Game' |

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

