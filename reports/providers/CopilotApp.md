# CopilotApp

- **Label:** Copilot App
- **URL:** https://play.google.com/store/apps/details?id=com.microsoft.copilot
- **Models:** 5
- **Working tests:** 4 / 5
- **Avg response time:** 1.36s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `chat` | text | ✅ `ok` | 1.08s | contains expected token 'PONG' |
| `reasoning` | text | ✅ `ok` | 2.67s | contains expected token 'PONG' |
| `search` | text | ✅ `ok` | 0.70s | contains expected token 'PONG' |
| `smart` | text | ✅ `ok` | 1.00s | contains expected token 'PONG' |
| `study` | text | ❌ `invalid` | 2.62s | expected 'PONG', got: 'I can do that — but since you’re in **Study Mode**, I need to check one thing fi' |

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

