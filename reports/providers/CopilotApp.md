# CopilotApp

- **Label:** Copilot App
- **URL:** https://play.google.com/store/apps/details?id=com.microsoft.copilot
- **Models:** 7
- **Working tests:** 6 / 7
- **Avg response time:** 0.97s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `chat` | text | ✅ `ok` | 1.07s | contains expected token 'PONG' |
| `gpt-4` | text | ✅ `ok` | 1.41s | contains expected token 'PONG' |
| `gpt-4o` | text | ✅ `ok` | 0.76s | contains expected token 'PONG' |
| `reasoning` | text | ✅ `ok` | 1.02s | contains expected token 'PONG' |
| `search` | text | ✅ `ok` | 0.75s | contains expected token 'PONG' |
| `smart` | text | ✅ `ok` | 0.84s | contains expected token 'PONG' |
| `study` | text | ❌ `invalid` | 2.44s | expected 'PONG', got: 'Since you’re in **Study Mode**, I can’t just follow a command to output a specif' |

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

