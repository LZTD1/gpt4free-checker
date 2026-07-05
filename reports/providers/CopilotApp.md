# CopilotApp

- **Label:** Copilot App
- **URL:** https://play.google.com/store/apps/details?id=com.microsoft.copilot
- **Models:** 5
- **Working tests:** 4 / 5
- **Avg response time:** 2.31s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `chat` | text | ✅ `ok` | 1.43s | contains expected token 'PONG' |
| `reasoning` | text | ✅ `ok` | 5.76s | contains expected token 'PONG' |
| `search` | text | ✅ `ok` | 0.74s | contains expected token 'PONG' |
| `smart` | text | ✅ `ok` | 1.32s | contains expected token 'PONG' |
| `study` | text | ❌ `invalid` | 2.85s | expected 'PONG', got: 'It looks like you’re asking me to output exactly one word — **but** since you’re' |

## Sample successful responses

### `smart` — text

```
PONG
```

### `reasoning` — text

```
PONG
```

### `chat` — text

```
PONG
```

### `search` — text

```
PONG
```

