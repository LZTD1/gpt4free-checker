# CopilotApp

- **Label:** Copilot App
- **URL:** https://play.google.com/store/apps/details?id=com.microsoft.copilot
- **Models:** 7
- **Working tests:** 6 / 7
- **Avg response time:** 1.00s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `chat` | text | ✅ `ok` | 1.16s | contains expected token 'PONG' |
| `gpt-4` | text | ✅ `ok` | 1.06s | contains expected token 'PONG' |
| `gpt-4o` | text | ✅ `ok` | 0.96s | contains expected token 'PONG' |
| `reasoning` | text | ✅ `ok` | 0.99s | contains expected token 'PONG' |
| `search` | text | ✅ `ok` | 0.70s | contains expected token 'PONG' |
| `smart` | text | ✅ `ok` | 1.13s | contains expected token 'PONG' |
| `study` | text | ❌ `invalid` | 4.60s | expected 'PONG', got: 'Since you’re in **Study Mode**, I can’t just follow a command to output a single' |

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

