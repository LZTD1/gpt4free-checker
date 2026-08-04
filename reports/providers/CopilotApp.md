# CopilotApp

- **Label:** Copilot App
- **URL:** https://play.google.com/store/apps/details?id=com.microsoft.copilot
- **Models:** 5
- **Working tests:** 3 / 5
- **Avg response time:** 0.77s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `chat` | text | ✅ `ok` | 0.78s | contains expected token 'PONG' |
| `search` | text | ✅ `ok` | 0.71s | contains expected token 'PONG' |
| `smart` | text | ✅ `ok` | 0.82s | contains expected token 'PONG' |
| `reasoning` | text | ❌ `exception` | 0.11s | WSServerHandshakeError: 460, message='Invalid response status', url='wss://copilot.microsoft.com/c/api/chat?api-version=2&clientSessionId=a4c3c411-7372-4b13-b4f |
| `study` | text | ❌ `invalid` | 20.31s | expected 'PONG', got: 'It looks like you’re asking for a **single‑word reply**, but you’re also in **St' |

## Sample successful responses

### `smart` — text

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

