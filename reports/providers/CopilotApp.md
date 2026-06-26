# CopilotApp

- **Label:** Copilot App
- **URL:** https://play.google.com/store/apps/details?id=com.microsoft.copilot
- **Models:** 7
- **Working tests:** 6 / 7
- **Avg response time:** 1.31s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `chat` | text | ✅ `ok` | 2.13s | contains expected token 'PONG' |
| `gpt-4` | text | ✅ `ok` | 1.16s | contains expected token 'PONG' |
| `gpt-4o` | text | ✅ `ok` | 0.88s | contains expected token 'PONG' |
| `reasoning` | text | ✅ `ok` | 1.12s | contains expected token 'PONG' |
| `search` | text | ✅ `ok` | 0.80s | contains expected token 'PONG' |
| `smart` | text | ✅ `ok` | 1.74s | contains expected token 'PONG' |
| `study` | text | ❌ `invalid` | 5.51s | expected 'PONG', got: 'It looks like you’re asking for a very specific one‑word reply — but since you’r' |

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

