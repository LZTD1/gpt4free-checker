# CohereForAI_C4AI_Command

- **Label:** CohereForAI C4AI Command
- **URL:** https://coherelabs-c4ai-command.hf.space
- **Models:** 7
- **Working tests:** 3 / 7
- **Avg response time:** 42.92s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `command-r-plus-08-2024` | text | ✅ `ok` | 42.56s | contains expected token 'PONG' |
| `command-r7b-12-2024` | text | ✅ `ok` | 42.30s | contains expected token 'PONG' |
| `command-r7b-arabic-02-2025` | text | ✅ `ok` | 43.89s | contains expected token 'PONG' |
| `command-a-03-2025` | text | ❌ `invalid` | 22.88s | expected 'PONG', got: 'PING' |
| `command-r` | text | ❌ `empty` | 22.03s | Empty response |
| `command-r-08-2024` | text | ❌ `timeout` | 64.85s | Timeout limit exceeded |
| `command-r-plus` | text | ❌ `timeout` | 64.64s | Timeout limit exceeded |

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

