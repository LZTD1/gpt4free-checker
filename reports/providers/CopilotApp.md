# CopilotApp

- **Label:** Copilot App
- **URL:** https://play.google.com/store/apps/details?id=com.microsoft.copilot
- **Models:** 5
- **Working tests:** 4 / 5
- **Avg response time:** 1.00s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `chat` | text | ✅ `ok` | 1.11s | contains expected token 'PONG' |
| `reasoning` | text | ✅ `ok` | 1.24s | contains expected token 'PONG' |
| `search` | text | ✅ `ok` | 0.67s | contains expected token 'PONG' |
| `smart` | text | ✅ `ok` | 0.96s | contains expected token 'PONG' |
| `study` | text | ❌ `invalid` | 2.13s | expected 'PONG', got: 'I see you’re asking for **exactly one word**, but since you’re in **Study Mode**' |

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

