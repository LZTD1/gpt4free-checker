# CopilotApp

- **Label:** Copilot App
- **URL:** https://play.google.com/store/apps/details?id=com.microsoft.copilot
- **Models:** 5
- **Working tests:** 5 / 5
- **Avg response time:** 2.22s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `chat` | text | ✅ `ok` | 1.49s | contains expected token 'PONG' |
| `reasoning` | text | ✅ `ok` | 4.71s | contains expected token 'PONG' |
| `search` | text | ✅ `ok` | 0.76s | contains expected token 'PONG' |
| `smart` | text | ✅ `ok` | 0.74s | contains expected token 'PONG' |
| `study` | text | ✅ `ok` | 3.40s | contains expected token 'PONG' |

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
I can do that — but since you’re in **Study Mode**, I need to check one thing first.

You asked me to **reply with exact
```

### `search` — text

```
PONG
```

