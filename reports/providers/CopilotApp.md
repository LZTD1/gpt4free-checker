# CopilotApp

- **Label:** Copilot App
- **URL:** https://play.google.com/store/apps/details?id=com.microsoft.copilot
- **Models:** 5
- **Working tests:** 5 / 5
- **Avg response time:** 4.91s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `chat` | text | ✅ `ok` | 0.85s | contains expected token 'PONG' |
| `reasoning` | text | ✅ `ok` | 1.21s | contains expected token 'PONG' |
| `search` | text | ✅ `ok` | 0.62s | contains expected token 'PONG' |
| `smart` | text | ✅ `ok` | 0.84s | contains expected token 'PONG' |
| `study` | text | ✅ `ok` | 21.03s | contains expected token 'PONG' |

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
It looks like you’re asking me to output exactly one word — but since you’re in **Study mode**, I’m not allowed to simpl
```

### `search` — text

```
PONG
```

