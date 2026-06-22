# CopilotApp

- **Label:** Copilot App
- **URL:** https://play.google.com/store/apps/details?id=com.microsoft.copilot
- **Models:** 7
- **Working tests:** 6 / 7
- **Avg response time:** 1.17s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `chat` | text | ✅ `ok` | 1.20s | contains expected token 'PONG' |
| `gpt-4` | text | ✅ `ok` | 1.12s | contains expected token 'PONG' |
| `gpt-4o` | text | ✅ `ok` | 1.46s | contains expected token 'PONG' |
| `reasoning` | text | ✅ `ok` | 1.07s | contains expected token 'PONG' |
| `search` | text | ✅ `ok` | 1.07s | contains expected token 'PONG' |
| `smart` | text | ✅ `ok` | 1.08s | contains expected token 'PONG' |
| `study` | text | ❌ `invalid` | 8.22s | expected 'PONG', got: 'It looks like you’re asking for a **single‑word output**, but since you’re in **' |

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

