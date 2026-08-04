# CopilotApp

- **Label:** Copilot App
- **URL:** https://play.google.com/store/apps/details?id=com.microsoft.copilot
- **Models:** 5
- **Working tests:** 4 / 5
- **Avg response time:** 1.00s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `chat` | text | ✅ `ok` | 0.92s | contains expected token 'PONG' |
| `reasoning` | text | ✅ `ok` | 1.37s | contains expected token 'PONG' |
| `search` | text | ✅ `ok` | 0.61s | contains expected token 'PONG' |
| `smart` | text | ✅ `ok` | 1.12s | contains expected token 'PONG' |
| `study` | text | ❌ `invalid` | 1.60s | expected 'PONG', got: 'It looks like you’re asking for a **single‑word reply**, but you’re also in **St' |

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

