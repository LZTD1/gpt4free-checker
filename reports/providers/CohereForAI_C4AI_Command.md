# CohereForAI_C4AI_Command

- **Label:** CohereForAI C4AI Command
- **URL:** https://coherelabs-c4ai-command.hf.space
- **Models:** 7
- **Working tests:** 1 / 7
- **Avg response time:** 43.92s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `command-r-plus-08-2024` | text | ✅ `ok` | 43.92s | contains expected token 'PONG' |
| `command-a-03-2025` | text | ❌ `timeout` | 45.00s | Timeout limit exceeded |
| `command-r` | text | ❌ `timeout` | 64.72s | Timeout limit exceeded |
| `command-r-08-2024` | text | ❌ `invalid` | 43.74s | expected 'PONG', got: 'Ping' |
| `command-r-plus` | text | ❌ `empty` | 43.99s | Empty response |
| `command-r7b-12-2024` | text | ❌ `timeout` | 63.26s | Timeout limit exceeded |
| `command-r7b-arabic-02-2025` | text | ❌ `timeout` | 45.00s | Timeout limit exceeded |

## Sample successful responses

### `command-r-plus-08-2024` — text

```
PONG
```

