# CopilotApp

- **Label:** Copilot App
- **URL:** https://play.google.com/store/apps/details?id=com.microsoft.copilot
- **Models:** 7
- **Working tests:** 6 / 7
- **Avg response time:** 1.08s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `chat` | text | ✅ `ok` | 1.58s | contains expected token 'PONG' |
| `gpt-4` | text | ✅ `ok` | 0.95s | contains expected token 'PONG' |
| `gpt-4o` | text | ✅ `ok` | 1.08s | contains expected token 'PONG' |
| `reasoning` | text | ✅ `ok` | 1.27s | contains expected token 'PONG' |
| `search` | text | ✅ `ok` | 0.68s | contains expected token 'PONG' |
| `smart` | text | ✅ `ok` | 0.91s | contains expected token 'PONG' |
| `study` | text | ❌ `invalid` | 3.74s | expected 'PONG', got: 'It looks like you’re asking for a very specific output — **one exact word** — bu' |

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

