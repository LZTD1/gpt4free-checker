# CopilotApp

- **Label:** Copilot App
- **URL:** https://play.google.com/store/apps/details?id=com.microsoft.copilot
- **Models:** 7
- **Working tests:** 6 / 7
- **Avg response time:** 1.54s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `chat` | text | ✅ `ok` | 1.42s | contains expected token 'PONG' |
| `gpt-4` | text | ✅ `ok` | 3.30s | contains expected token 'PONG' |
| `gpt-4o` | text | ✅ `ok` | 1.08s | contains expected token 'PONG' |
| `reasoning` | text | ✅ `ok` | 1.52s | contains expected token 'PONG' |
| `search` | text | ✅ `ok` | 0.77s | contains expected token 'PONG' |
| `smart` | text | ✅ `ok` | 1.15s | contains expected token 'PONG' |
| `study` | text | ❌ `invalid` | 12.25s | expected 'PONG', got: 'Since you’re in **Study Mode**, I can’t just obey a command without understandin' |

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

