# CopilotApp

- **Label:** Copilot App
- **URL:** https://play.google.com/store/apps/details?id=com.microsoft.copilot
- **Models:** 5
- **Working tests:** 4 / 5
- **Avg response time:** 0.93s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `chat` | text | ✅ `ok` | 1.01s | contains expected token 'PONG' |
| `reasoning` | text | ✅ `ok` | 1.27s | contains expected token 'PONG' |
| `search` | text | ✅ `ok` | 0.65s | contains expected token 'PONG' |
| `smart` | text | ✅ `ok` | 0.81s | contains expected token 'PONG' |
| `study` | text | ❌ `invalid` | 3.42s | expected 'PONG', got: 'It looks like you’re asking for a **single-word reply**, but since you’re in **S' |

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

