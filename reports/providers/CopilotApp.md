# CopilotApp

- **Label:** Copilot App
- **URL:** https://play.google.com/store/apps/details?id=com.microsoft.copilot
- **Models:** 7
- **Working tests:** 6 / 7
- **Avg response time:** 1.43s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `chat` | text | ✅ `ok` | 1.17s | contains expected token 'PONG' |
| `gpt-4` | text | ✅ `ok` | 1.49s | contains expected token 'PONG' |
| `gpt-4o` | text | ✅ `ok` | 2.26s | contains expected token 'PONG' |
| `reasoning` | text | ✅ `ok` | 1.31s | contains expected token 'PONG' |
| `search` | text | ✅ `ok` | 0.95s | contains expected token 'PONG' |
| `smart` | text | ✅ `ok` | 1.40s | contains expected token 'PONG' |
| `study` | text | ❌ `invalid` | 4.51s | expected 'PONG', got: 'It looks like you’re giving me an instruction rather than asking something you w' |

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

