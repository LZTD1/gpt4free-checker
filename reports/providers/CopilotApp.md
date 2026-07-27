# CopilotApp

- **Label:** Copilot App
- **URL:** https://play.google.com/store/apps/details?id=com.microsoft.copilot
- **Models:** 5
- **Working tests:** 4 / 5
- **Avg response time:** 10.93s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `chat` | text | ✅ `ok` | 0.95s | contains expected token 'PONG' |
| `reasoning` | text | ✅ `ok` | 21.07s | contains expected token 'PONG' |
| `search` | text | ✅ `ok` | 0.66s | contains expected token 'PONG' |
| `smart` | text | ✅ `ok` | 21.04s | contains expected token 'PONG' |
| `study` | text | ❌ `invalid` | 1.78s | expected 'PONG', got: 'It looks like you’re asking me to reply with exactly one word — **but** in Study' |

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

