# CopilotApp

- **Label:** Copilot App
- **URL:** https://play.google.com/store/apps/details?id=com.microsoft.copilot
- **Models:** 5
- **Working tests:** 4 / 5
- **Avg response time:** 0.84s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `chat` | text | ✅ `ok` | 0.73s | contains expected token 'PONG' |
| `reasoning` | text | ✅ `ok` | 1.07s | contains expected token 'PONG' |
| `search` | text | ✅ `ok` | 0.68s | contains expected token 'PONG' |
| `smart` | text | ✅ `ok` | 0.86s | contains expected token 'PONG' |
| `study` | text | ❌ `invalid` | 2.19s | expected 'PONG', got: "It looks like you want a **single word**, but since you're in **Study Mode**, I " |

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

