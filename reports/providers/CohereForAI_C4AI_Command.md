# CohereForAI_C4AI_Command

- **Label:** CohereForAI C4AI Command
- **URL:** https://coherelabs-c4ai-command.hf.space
- **Models:** 7
- **Working tests:** 2 / 7
- **Avg response time:** 11.48s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `command-r-plus-08-2024` | text | ✅ `ok` | 22.18s | contains expected token 'PONG' |
| `command-r7b-12-2024` | text | ✅ `ok` | 0.78s | contains expected token 'PONG' |
| `command-a-03-2025` | text | ❌ `invalid` | 0.51s | expected 'PONG', got: 'PING' |
| `command-r` | text | ❌ `empty` | 0.93s | Empty response |
| `command-r-08-2024` | text | ❌ `invalid` | 0.98s | expected 'PONG', got: 'Ping' |
| `command-r-plus` | text | ❌ `empty` | 1.05s | Empty response |
| `command-r7b-arabic-02-2025` | text | ❌ `timeout` | 45.00s | Timeout limit exceeded |

## Sample successful responses

### `command-r-plus-08-2024` — text

```
PONG
```

### `command-r7b-12-2024` — text

```
PONG
```

