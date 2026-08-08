# CopilotApp

- **Label:** Copilot App
- **URL:** https://play.google.com/store/apps/details?id=com.microsoft.copilot
- **Models:** 5
- **Working tests:** 5 / 5
- **Avg response time:** 4.90s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `chat` | text | ✅ `ok` | 0.86s | contains expected token 'PONG' |
| `reasoning` | text | ✅ `ok` | 1.04s | contains expected token 'PONG' |
| `search` | text | ✅ `ok` | 0.75s | contains expected token 'PONG' |
| `smart` | text | ✅ `ok` | 0.83s | contains expected token 'PONG' |
| `study` | text | ✅ `ok` | 21.04s | contains expected token 'PONG' |

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

Si
```

### `search` — text

```
PONG
```

