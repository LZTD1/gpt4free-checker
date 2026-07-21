# CopilotApp

- **Label:** Copilot App
- **URL:** https://play.google.com/store/apps/details?id=com.microsoft.copilot
- **Models:** 5
- **Working tests:** 4 / 5
- **Avg response time:** 6.01s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `chat` | text | ✅ `ok` | 1.44s | contains expected token 'PONG' |
| `reasoning` | text | ✅ `ok` | 1.35s | contains expected token 'PONG' |
| `search` | text | ✅ `ok` | 20.32s | contains expected token 'PONG' |
| `smart` | text | ✅ `ok` | 0.91s | contains expected token 'PONG' |
| `study` | text | ❌ `invalid` | 21.03s | expected 'PONG', got: 'It looks like you’re giving me a very specific instruction, but since you’re in ' |

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

