# CopilotApp

- **Label:** Copilot App
- **URL:** https://play.google.com/store/apps/details?id=com.microsoft.copilot
- **Models:** 5
- **Working tests:** 4 / 5
- **Avg response time:** 1.03s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `chat` | text | ✅ `ok` | 0.94s | contains expected token 'PONG' |
| `reasoning` | text | ✅ `ok` | 1.41s | contains expected token 'PONG' |
| `search` | text | ✅ `ok` | 0.82s | contains expected token 'PONG' |
| `smart` | text | ✅ `ok` | 0.96s | contains expected token 'PONG' |
| `study` | text | ❌ `exception` | 20.21s | ClientConnectionResetError: Cannot write to closing transport |

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

