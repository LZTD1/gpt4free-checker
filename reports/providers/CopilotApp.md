# CopilotApp

- **Label:** Copilot App
- **URL:** https://play.google.com/store/apps/details?id=com.microsoft.copilot
- **Models:** 5
- **Working tests:** 5 / 5
- **Avg response time:** 1.14s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `chat` | text | ✅ `ok` | 1.12s | contains expected token 'PONG' |
| `reasoning` | text | ✅ `ok` | 1.07s | contains expected token 'PONG' |
| `search` | text | ✅ `ok` | 0.74s | contains expected token 'PONG' |
| `smart` | text | ✅ `ok` | 1.02s | contains expected token 'PONG' |
| `study` | text | ✅ `ok` | 1.74s | contains expected token 'PONG' |

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
It looks like you’re giving me a very strict instruction — **“Reply with exactly one word and nothing else: PONG.”**  


```

### `search` — text

```
PONG
```

