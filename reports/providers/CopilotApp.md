# CopilotApp

- **Label:** Copilot App
- **URL:** https://play.google.com/store/apps/details?id=com.microsoft.copilot
- **Models:** 5
- **Working tests:** 5 / 5
- **Avg response time:** 21.04s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `chat` | text | ✅ `ok` | 20.84s | contains expected token 'PONG' |
| `reasoning` | text | ✅ `ok` | 20.22s | contains expected token 'PONG' |
| `search` | text | ✅ `ok` | 21.07s | contains expected token 'PONG' |
| `smart` | text | ✅ `ok` | 21.03s | contains expected token 'PONG' |
| `study` | text | ✅ `ok` | 22.03s | contains expected token 'PONG' |

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
Before I reply, I need to check one thing with you because you’re in **Study Mode**.

Study Mode requires me to guide yo
```

### `search` — text

```
PONG
```

