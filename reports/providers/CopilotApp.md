# CopilotApp

- **Label:** Copilot App
- **URL:** https://play.google.com/store/apps/details?id=com.microsoft.copilot
- **Models:** 5
- **Working tests:** 5 / 5
- **Avg response time:** 4.85s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `chat` | text | ✅ `ok` | 0.90s | contains expected token 'PONG' |
| `reasoning` | text | ✅ `ok` | 0.94s | contains expected token 'PONG' |
| `search` | text | ✅ `ok` | 0.67s | contains expected token 'PONG' |
| `smart` | text | ✅ `ok` | 0.76s | contains expected token 'PONG' |
| `study` | text | ✅ `ok` | 21.00s | contains expected token 'PONG' |

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
It looks like you’re asking me to reply with exactly one word — **PONG** — and nothing else.

Since you’re in **Study Mo
```

### `search` — text

```
PONG
```

