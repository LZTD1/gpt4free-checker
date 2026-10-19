# CohereForAI_C4AI_Command

- **Label:** CohereForAI C4AI Command
- **URL:** https://coherelabs-c4ai-command.hf.space
- **Models:** 7
- **Working tests:** 3 / 7
- **Avg response time:** 36.61s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `command-a-03-2025` | text | ✅ `ok` | 21.75s | contains expected token 'PONG' |
| `command-r-plus-08-2024` | text | ✅ `ok` | 43.91s | contains expected token 'PONG' |
| `command-r7b-12-2024` | text | ✅ `ok` | 44.16s | contains expected token 'PONG' |
| `command-r` | text | ❌ `empty` | 21.97s | Empty response |
| `command-r-08-2024` | text | ❌ `invalid` | 43.31s | expected 'PONG', got: 'Ping' |
| `command-r-plus` | text | ❌ `empty` | 43.05s | Empty response |
| `command-r7b-arabic-02-2025` | text | ❌ `timeout` | 45.00s | Timeout limit exceeded |

## Sample successful responses

### `command-a-03-2025` — text

```
PONG
```

### `command-r-plus-08-2024` — text

```
PONG
```

### `command-r7b-12-2024` — text

```
PONG
```

