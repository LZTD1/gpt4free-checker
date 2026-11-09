# CohereForAI_C4AI_Command

- **Label:** CohereForAI C4AI Command
- **URL:** https://coherelabs-c4ai-command.hf.space
- **Models:** 7
- **Working tests:** 2 / 7
- **Avg response time:** 10.52s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `command-r-plus-08-2024` | text | ✅ `ok` | 20.53s | contains expected token 'PONG' |
| `command-r7b-12-2024` | text | ✅ `ok` | 0.51s | contains expected token 'PONG' |
| `command-a-03-2025` | text | ❌ `invalid` | 22.03s | expected 'PONG', got: 'PING' |
| `command-r` | text | ❌ `empty` | 0.48s | Empty response |
| `command-r-08-2024` | text | ❌ `timeout` | 45.00s | Timeout limit exceeded |
| `command-r-plus` | text | ❌ `empty` | 0.38s | Empty response |
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

