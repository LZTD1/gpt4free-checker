# CopilotApp

- **Label:** Copilot App
- **URL:** https://play.google.com/store/apps/details?id=com.microsoft.copilot
- **Models:** 5
- **Working tests:** 5 / 5
- **Avg response time:** 1.35s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `chat` | text | ✅ `ok` | 0.83s | contains expected token 'PONG' |
| `reasoning` | text | ✅ `ok` | 1.07s | contains expected token 'PONG' |
| `search` | text | ✅ `ok` | 0.95s | contains expected token 'PONG' |
| `smart` | text | ✅ `ok` | 1.42s | contains expected token 'PONG' |
| `study` | text | ✅ `ok` | 2.49s | contains expected token 'PONG' |

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
Before I answer, I need to check one thing with you because you’re in **Study Mode**.

A request like **“Reply with exac
```

### `search` — text

```
PONG
```

