# CopilotApp

- **Label:** Copilot App
- **URL:** https://play.google.com/store/apps/details?id=com.microsoft.copilot
- **Models:** 7
- **Working tests:** 6 / 7
- **Avg response time:** 1.00s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `chat` | text | ✅ `ok` | 1.05s | contains expected token 'PONG' |
| `gpt-4` | text | ✅ `ok` | 0.92s | contains expected token 'PONG' |
| `gpt-4o` | text | ✅ `ok` | 0.95s | contains expected token 'PONG' |
| `reasoning` | text | ✅ `ok` | 1.42s | contains expected token 'PONG' |
| `search` | text | ✅ `ok` | 0.76s | contains expected token 'PONG' |
| `smart` | text | ✅ `ok` | 0.90s | contains expected token 'PONG' |
| `study` | text | ❌ `invalid` | 4.09s | expected 'PONG', got: 'It looks like you’re giving me an instruction, but since you’re in **Study Mode*' |

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

