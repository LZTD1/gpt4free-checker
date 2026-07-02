# CopilotApp

- **Label:** Copilot App
- **URL:** https://play.google.com/store/apps/details?id=com.microsoft.copilot
- **Models:** 5
- **Working tests:** 4 / 5
- **Avg response time:** 1.05s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `chat` | text | ✅ `ok` | 1.41s | contains expected token 'PONG' |
| `reasoning` | text | ✅ `ok` | 1.04s | contains expected token 'PONG' |
| `search` | text | ✅ `ok` | 0.74s | contains expected token 'PONG' |
| `smart` | text | ✅ `ok` | 1.02s | contains expected token 'PONG' |
| `study` | text | ❌ `invalid` | 5.81s | expected 'PONG', got: "It looks like you want me to reply with exactly one word — **but** because you'r" |

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

