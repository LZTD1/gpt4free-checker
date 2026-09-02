# CohereForAI_C4AI_Command

- **Label:** CohereForAI C4AI Command
- **URL:** https://coherelabs-c4ai-command.hf.space
- **Models:** 7
- **Working tests:** 3 / 7
- **Avg response time:** 42.94s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `command-r-plus-08-2024` | text | ✅ `ok` | 43.05s | contains expected token 'PONG' |
| `command-r7b-12-2024` | text | ✅ `ok` | 42.83s | contains expected token 'PONG' |
| `command-r7b-arabic-02-2025` | text | ✅ `ok` | 42.94s | contains expected token 'PONG' |
| `command-a-03-2025` | text | ❌ `invalid` | 44.86s | expected 'PONG', got: 'PING' |
| `command-r` | text | ❌ `timeout` | 64.65s | Timeout limit exceeded |
| `command-r-08-2024` | text | ❌ `invalid` | 42.78s | expected 'PONG', got: 'Ping' |
| `command-r-plus` | text | ❌ `empty` | 43.67s | Empty response |

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

