# CopilotApp

- **Label:** Copilot App
- **URL:** https://play.google.com/store/apps/details?id=com.microsoft.copilot
- **Models:** 5
- **Working tests:** 4 / 5
- **Avg response time:** 0.95s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `chat` | text | ✅ `ok` | 0.96s | contains expected token 'PONG' |
| `reasoning` | text | ✅ `ok` | 1.13s | contains expected token 'PONG' |
| `search` | text | ✅ `ok` | 0.68s | contains expected token 'PONG' |
| `smart` | text | ✅ `ok` | 1.05s | contains expected token 'PONG' |
| `study` | text | ❌ `invalid` | 1.75s | expected 'PONG', got: "Before I reply: you're in **Study mode**, and one of the strict rules is that I " |

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

