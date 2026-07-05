# WeWordle

- **Label:** WeWordle
- **URL:** https://chat-gpt.com
- **Models:** 7
- **Working tests:** 5 / 7
- **Avg response time:** 2.29s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `deepseek` | text | ✅ `ok` | 1.44s | contains expected token 'PONG' |
| `deepseek-r1` | text | ✅ `ok` | 4.03s | contains expected token 'PONG' |
| `deepseek-reasoner` | text | ✅ `ok` | 1.75s | contains expected token 'PONG' |
| `gpt-4` | text | ✅ `ok` | 1.41s | contains expected token 'PONG' |
| `v3` | text | ✅ `ok` | 2.84s | contains expected token 'PONG' |
| `gpt-4o` | text | ❌ `invalid` | 1.62s | expected 'PONG', got: 'PING' |
| `gpt-4o-mini` | text | ❌ `invalid` | 1.14s | expected 'PONG', got: 'Ping' |

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

