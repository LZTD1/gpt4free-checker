# CopilotApp

- **Label:** Copilot App
- **URL:** https://play.google.com/store/apps/details?id=com.microsoft.copilot
- **Models:** 5
- **Working tests:** 4 / 5
- **Avg response time:** 0.88s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `chat` | text | ✅ `ok` | 0.81s | contains expected token 'PONG' |
| `reasoning` | text | ✅ `ok` | 1.12s | contains expected token 'PONG' |
| `search` | text | ✅ `ok` | 0.70s | contains expected token 'PONG' |
| `smart` | text | ✅ `ok` | 0.87s | contains expected token 'PONG' |
| `study` | text | ❌ `invalid` | 21.03s | expected 'PONG', got: "It looks like you want a single-word reply, but you're also in **Study mode**, w" |

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

