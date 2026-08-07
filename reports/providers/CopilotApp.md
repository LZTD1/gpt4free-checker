# CopilotApp

- **Label:** Copilot App
- **URL:** https://play.google.com/store/apps/details?id=com.microsoft.copilot
- **Models:** 5
- **Working tests:** 4 / 5
- **Avg response time:** 11.25s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `chat` | text | ✅ `ok` | 20.50s | contains expected token 'PONG' |
| `reasoning` | text | ✅ `ok` | 22.04s | contains expected token 'PONG' |
| `search` | text | ✅ `ok` | 1.59s | contains expected token 'PONG' |
| `smart` | text | ✅ `ok` | 0.86s | contains expected token 'PONG' |
| `study` | text | ❌ `invalid` | 20.43s | expected 'PONG', got: 'It looks like you’re asking for a **single‑word reply**, but you’re also in **St' |

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

