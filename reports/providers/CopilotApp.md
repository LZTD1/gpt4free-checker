# CopilotApp

- **Label:** Copilot App
- **URL:** https://play.google.com/store/apps/details?id=com.microsoft.copilot
- **Models:** 7
- **Working tests:** 6 / 7
- **Avg response time:** 1.33s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `chat` | text | ✅ `ok` | 1.17s | contains expected token 'PONG' |
| `gpt-4` | text | ✅ `ok` | 1.45s | contains expected token 'PONG' |
| `gpt-4o` | text | ✅ `ok` | 2.11s | contains expected token 'PONG' |
| `reasoning` | text | ✅ `ok` | 1.28s | contains expected token 'PONG' |
| `search` | text | ✅ `ok` | 0.79s | contains expected token 'PONG' |
| `smart` | text | ✅ `ok` | 1.15s | contains expected token 'PONG' |
| `study` | text | ❌ `invalid` | 3.06s | expected 'PONG', got: 'I can’t do that in Study mode, but I *can* help you learn or practice something.' |

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

### `gpt-4` — text

```
PONG
```

### `gpt-4o` — text

```
PONG
```

