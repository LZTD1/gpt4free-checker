# CopilotApp

- **Label:** Copilot App
- **URL:** https://play.google.com/store/apps/details?id=com.microsoft.copilot
- **Models:** 5
- **Working tests:** 4 / 5
- **Avg response time:** 0.98s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `chat` | text | ✅ `ok` | 0.82s | contains expected token 'PONG' |
| `reasoning` | text | ✅ `ok` | 1.53s | contains expected token 'PONG' |
| `search` | text | ✅ `ok` | 0.72s | contains expected token 'PONG' |
| `smart` | text | ✅ `ok` | 0.87s | contains expected token 'PONG' |
| `study` | text | ❌ `invalid` | 4.83s | expected 'PONG', got: "It looks like you want me to reply with exactly one word — **but** because you'r" |

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

