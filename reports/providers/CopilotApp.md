# CopilotApp

- **Label:** Copilot App
- **URL:** https://play.google.com/store/apps/details?id=com.microsoft.copilot
- **Models:** 5
- **Working tests:** 5 / 5
- **Avg response time:** 1.73s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `chat` | text | ✅ `ok` | 0.99s | contains expected token 'PONG' |
| `reasoning` | text | ✅ `ok` | 1.24s | contains expected token 'PONG' |
| `search` | text | ✅ `ok` | 0.61s | contains expected token 'PONG' |
| `smart` | text | ✅ `ok` | 2.73s | contains expected token 'PONG' |
| `study` | text | ✅ `ok` | 3.09s | contains expected token 'PONG' |

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

