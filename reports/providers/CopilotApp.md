# CopilotApp

- **Label:** Copilot App
- **URL:** https://play.google.com/store/apps/details?id=com.microsoft.copilot
- **Models:** 7
- **Working tests:** 6 / 7
- **Avg response time:** 0.98s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `chat` | text | ✅ `ok` | 1.00s | contains expected token 'PONG' |
| `gpt-4` | text | ✅ `ok` | 0.87s | contains expected token 'PONG' |
| `gpt-4o` | text | ✅ `ok` | 1.03s | contains expected token 'PONG' |
| `reasoning` | text | ✅ `ok` | 1.13s | contains expected token 'PONG' |
| `search` | text | ✅ `ok` | 0.70s | contains expected token 'PONG' |
| `smart` | text | ✅ `ok` | 1.17s | contains expected token 'PONG' |
| `study` | text | ❌ `invalid` | 5.48s | expected 'PONG', got: 'It looks like you’re giving me a very strict instruction — **but since you’re in' |

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

