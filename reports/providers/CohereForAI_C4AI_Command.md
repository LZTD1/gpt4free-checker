# CohereForAI_C4AI_Command

- **Label:** CohereForAI C4AI Command
- **URL:** https://coherelabs-c4ai-command.hf.space
- **Models:** 7
- **Working tests:** 3 / 7
- **Avg response time:** 29.24s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `command-r-plus-08-2024` | text | ✅ `ok` | 22.02s | contains expected token 'PONG' |
| `command-r7b-12-2024` | text | ✅ `ok` | 42.97s | contains expected token 'PONG' |
| `command-r7b-arabic-02-2025` | text | ✅ `ok` | 22.73s | contains expected token 'PONG' |
| `command-a-03-2025` | text | ❌ `invalid` | 43.03s | expected 'PONG', got: 'PING' |
| `command-r` | text | ❌ `timeout` | 64.77s | Timeout limit exceeded |
| `command-r-08-2024` | text | ❌ `timeout` | 64.71s | Timeout limit exceeded |
| `command-r-plus` | text | ❌ `timeout` | 64.78s | Timeout limit exceeded |

## Sample successful responses

### `command-r-plus-08-2024` — text

```
PONG
```

### `command-r7b-12-2024` — text

```
PONG
```

### `command-r7b-arabic-02-2025` — text

```
PONG
```

