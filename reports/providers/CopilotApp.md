# CopilotApp

- **Label:** Copilot App
- **URL:** https://play.google.com/store/apps/details?id=com.microsoft.copilot
- **Models:** 7
- **Working tests:** 6 / 7
- **Avg response time:** 1.16s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `chat` | text | ✅ `ok` | 1.40s | contains expected token 'PONG' |
| `gpt-4` | text | ✅ `ok` | 1.05s | contains expected token 'PONG' |
| `gpt-4o` | text | ✅ `ok` | 1.07s | contains expected token 'PONG' |
| `reasoning` | text | ✅ `ok` | 1.10s | contains expected token 'PONG' |
| `search` | text | ✅ `ok` | 1.37s | contains expected token 'PONG' |
| `smart` | text | ✅ `ok` | 0.96s | contains expected token 'PONG' |
| `study` | text | ❌ `invalid` | 6.10s | expected 'PONG', got: 'I hear your request — **exactly one word** — but since you’re in **Study Mode**,' |

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

