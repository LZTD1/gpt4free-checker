# CohereForAI_C4AI_Command

- **Label:** CohereForAI C4AI Command
- **URL:** https://coherelabs-c4ai-command.hf.space
- **Models:** 7
- **Working tests:** 1 / 7
- **Avg response time:** 0.76s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `command-r7b-arabic-02-2025` | text | ✅ `ok` | 0.76s | contains expected token 'PONG' |
| `command-a-03-2025` | text | ❌ `invalid` | 21.67s | expected 'PONG', got: 'PING' |
| `command-r` | text | ❌ `empty` | 0.52s | Empty response |
| `command-r-08-2024` | text | ❌ `invalid` | 22.01s | expected 'PONG', got: 'Ping' |
| `command-r-plus` | text | ❌ `empty` | 22.13s | Empty response |
| `command-r-plus-08-2024` | text | ❌ `timeout` | 64.90s | Timeout limit exceeded |
| `command-r7b-12-2024` | text | ❌ `timeout` | 45.00s | Timeout limit exceeded |

## Sample successful responses

### `command-r7b-arabic-02-2025` — text

```
PONG
```

