# CopilotApp

- **Label:** Copilot App
- **URL:** https://play.google.com/store/apps/details?id=com.microsoft.copilot
- **Models:** 7
- **Working tests:** 6 / 7
- **Avg response time:** 1.17s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `chat` | text | ✅ `ok` | 1.07s | contains expected token 'PONG' |
| `gpt-4` | text | ✅ `ok` | 1.14s | contains expected token 'PONG' |
| `gpt-4o` | text | ✅ `ok` | 1.08s | contains expected token 'PONG' |
| `reasoning` | text | ✅ `ok` | 1.27s | contains expected token 'PONG' |
| `search` | text | ✅ `ok` | 1.04s | contains expected token 'PONG' |
| `smart` | text | ✅ `ok` | 1.43s | contains expected token 'PONG' |
| `study` | text | ❌ `invalid` | 3.92s | expected 'PONG', got: 'Since we’re in Study Mode, I can’t just follow an instruction to “give exactly o' |

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

