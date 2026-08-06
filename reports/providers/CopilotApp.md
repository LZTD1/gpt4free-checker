# CopilotApp

- **Label:** Copilot App
- **URL:** https://play.google.com/store/apps/details?id=com.microsoft.copilot
- **Models:** 5
- **Working tests:** 5 / 5
- **Avg response time:** 5.54s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `chat` | text | ✅ `ok` | 0.95s | contains expected token 'PONG' |
| `reasoning` | text | ✅ `ok` | 1.11s | contains expected token 'PONG' |
| `search` | text | ✅ `ok` | 0.88s | contains expected token 'PONG' |
| `smart` | text | ✅ `ok` | 0.80s | contains expected token 'PONG' |
| `study` | text | ✅ `ok` | 23.94s | contains expected token 'PONG' |

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

### `study` — text

```
I see you’re asking for **exactly one word**, but since you’re in **Study mode**, I can’t just give the final answer out
```

### `search` — text

```
PONG
```

