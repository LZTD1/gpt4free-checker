# CohereForAI_C4AI_Command

- **Label:** CohereForAI C4AI Command
- **URL:** https://coherelabs-c4ai-command.hf.space
- **Models:** 7
- **Working tests:** 2 / 7
- **Avg response time:** 42.13s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `command-r-plus-08-2024` | text | ✅ `ok` | 42.90s | contains expected token 'PONG' |
| `command-r7b-12-2024` | text | ✅ `ok` | 41.36s | contains expected token 'PONG' |
| `command-a-03-2025` | text | ❌ `invalid` | 42.83s | expected 'PONG', got: 'PING' |
| `command-r` | text | ❌ `empty` | 43.05s | Empty response |
| `command-r-08-2024` | text | ❌ `invalid` | 41.22s | expected 'PONG', got: 'Ping' |
| `command-r-plus` | text | ❌ `empty` | 43.99s | Empty response |
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

