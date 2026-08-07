# CopilotApp

- **Label:** Copilot App
- **URL:** https://play.google.com/store/apps/details?id=com.microsoft.copilot
- **Models:** 5
- **Working tests:** 4 / 5
- **Avg response time:** 11.30s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `chat` | text | ✅ `ok` | 21.03s | contains expected token 'PONG' |
| `reasoning` | text | ✅ `ok` | 1.18s | contains expected token 'PONG' |
| `search` | text | ✅ `ok` | 1.94s | contains expected token 'PONG' |
| `smart` | text | ✅ `ok` | 21.03s | contains expected token 'PONG' |
| `study` | text | ❌ `exception` | 0.26s | WSServerHandshakeError: 460, message='Invalid response status', url='wss://copilot.microsoft.com/c/api/chat?api-version=2&clientSessionId=83039f6f-0801-4281-95c |

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

