# WeWordle

- **Label:** WeWordle
- **URL:** https://chat-gpt.com
- **Models:** 7
- **Working tests:** 6 / 7
- **Avg response time:** 3.24s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `deepseek` | text | ✅ `ok` | 2.97s | contains expected token 'PONG' |
| `deepseek-r1` | text | ✅ `ok` | 4.23s | contains expected token 'PONG' |
| `deepseek-reasoner` | text | ✅ `ok` | 4.05s | contains expected token 'PONG' |
| `gpt-4` | text | ✅ `ok` | 3.35s | contains expected token 'PONG' |
| `gpt-4o-mini` | text | ✅ `ok` | 2.54s | contains expected token 'PONG' |
| `v3` | text | ✅ `ok` | 2.29s | contains expected token 'PONG' |
| `gpt-4o` | text | ❌ `invalid` | 2.35s | expected 'PONG', got: 'PING' |

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

