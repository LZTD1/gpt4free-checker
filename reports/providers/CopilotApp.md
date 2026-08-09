# CopilotApp

- **Label:** Copilot App
- **URL:** https://play.google.com/store/apps/details?id=com.microsoft.copilot
- **Models:** 5
- **Working tests:** 4 / 5
- **Avg response time:** 0.82s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `chat` | text | ✅ `ok` | 0.74s | contains expected token 'PONG' |
| `reasoning` | text | ✅ `ok` | 1.08s | contains expected token 'PONG' |
| `search` | text | ✅ `ok` | 0.66s | contains expected token 'PONG' |
| `smart` | text | ✅ `ok` | 0.82s | contains expected token 'PONG' |
| `study` | text | ❌ `exception` | 20.14s | ClientConnectionResetError: Cannot write to closing transport |

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

