# CopilotApp

- **Label:** Copilot App
- **URL:** https://play.google.com/store/apps/details?id=com.microsoft.copilot
- **Models:** 7
- **Working tests:** 6 / 7
- **Avg response time:** 0.96s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `chat` | text | ✅ `ok` | 0.84s | contains expected token 'PONG' |
| `gpt-4` | text | ✅ `ok` | 0.87s | contains expected token 'PONG' |
| `gpt-4o` | text | ✅ `ok` | 0.85s | contains expected token 'PONG' |
| `reasoning` | text | ✅ `ok` | 1.37s | contains expected token 'PONG' |
| `search` | text | ✅ `ok` | 0.93s | contains expected token 'PONG' |
| `smart` | text | ✅ `ok` | 0.91s | contains expected token 'PONG' |
| `study` | text | ❌ `invalid` | 4.23s | expected 'PONG', got: 'Since you’re in **Study Mode**, I can’t just follow a command to output a single' |

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

