# CopilotApp

- **Label:** Copilot App
- **URL:** https://play.google.com/store/apps/details?id=com.microsoft.copilot
- **Models:** 5
- **Working tests:** 4 / 5
- **Avg response time:** 16.00s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `chat` | text | ✅ `ok` | 21.01s | contains expected token 'PONG' |
| `reasoning` | text | ✅ `ok` | 21.20s | contains expected token 'PONG' |
| `search` | text | ✅ `ok` | 0.74s | contains expected token 'PONG' |
| `smart` | text | ✅ `ok` | 21.03s | contains expected token 'PONG' |
| `study` | text | ❌ `exception` | 0.12s | WSServerHandshakeError: 460, message='Invalid response status', url='wss://copilot.microsoft.com/c/api/chat?api-version=2&clientSessionId=a7d7414d-1021-447b-9c8 |

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

