# CopilotApp

- **Label:** Copilot App
- **URL:** https://play.google.com/store/apps/details?id=com.microsoft.copilot
- **Models:** 7
- **Working tests:** 6 / 7
- **Avg response time:** 1.04s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `chat` | text | ✅ `ok` | 1.11s | contains expected token 'PONG' |
| `gpt-4` | text | ✅ `ok` | 1.48s | contains expected token 'PONG' |
| `gpt-4o` | text | ✅ `ok` | 1.01s | contains expected token 'PONG' |
| `reasoning` | text | ✅ `ok` | 0.94s | contains expected token 'PONG' |
| `search` | text | ✅ `ok` | 0.87s | contains expected token 'PONG' |
| `smart` | text | ✅ `ok` | 0.85s | contains expected token 'PONG' |
| `study` | text | ❌ `invalid` | 2.10s | expected 'PONG', got: 'It looks like you want a very specific one‑word reply — but since you’re in **St' |

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

