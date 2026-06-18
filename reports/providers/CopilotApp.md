# CopilotApp

- **Label:** Copilot App
- **URL:** https://play.google.com/store/apps/details?id=com.microsoft.copilot
- **Models:** 7
- **Working tests:** 6 / 7
- **Avg response time:** 1.27s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `chat` | text | ✅ `ok` | 1.27s | contains expected token 'PONG' |
| `gpt-4` | text | ✅ `ok` | 1.26s | contains expected token 'PONG' |
| `gpt-4o` | text | ✅ `ok` | 1.66s | contains expected token 'PONG' |
| `reasoning` | text | ✅ `ok` | 1.34s | contains expected token 'PONG' |
| `search` | text | ✅ `ok` | 1.00s | contains expected token 'PONG' |
| `smart` | text | ✅ `ok` | 1.09s | contains expected token 'PONG' |
| `study` | text | ❌ `invalid` | 8.68s | expected 'PONG', got: 'Since you’re in **Study mode**, I can’t just follow a command to output a specif' |

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

