# CopilotApp

- **Label:** Copilot App
- **URL:** https://play.google.com/store/apps/details?id=com.microsoft.copilot
- **Models:** 5
- **Working tests:** 5 / 5
- **Avg response time:** 5.16s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `chat` | text | ✅ `ok` | 1.00s | contains expected token 'PONG' |
| `reasoning` | text | ✅ `ok` | 0.98s | contains expected token 'PONG' |
| `search` | text | ✅ `ok` | 0.62s | contains expected token 'PONG' |
| `smart` | text | ✅ `ok` | 0.86s | contains expected token 'PONG' |
| `study` | text | ✅ `ok` | 22.34s | contains expected token 'PONG' |

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

### `study` — text

```
Before I answer, I need to check something with you because you’re currently in **Study Mode**.

You asked: **“Reply wit
```

### `search` — text

```
PONG
```

