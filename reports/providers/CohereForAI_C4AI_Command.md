# CohereForAI_C4AI_Command

- **Label:** CohereForAI C4AI Command
- **URL:** https://coherelabs-c4ai-command.hf.space
- **Models:** 7
- **Working tests:** 3 / 7
- **Avg response time:** 0.63s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `command-a-03-2025` | text | ✅ `ok` | 0.58s | contains expected token 'PONG' |
| `command-r-plus-08-2024` | text | ✅ `ok` | 0.80s | contains expected token 'PONG' |
| `command-r7b-12-2024` | text | ✅ `ok` | 0.50s | contains expected token 'PONG' |
| `command-r` | text | ❌ `empty` | 0.38s | Empty response |
| `command-r-08-2024` | text | ❌ `invalid` | 0.50s | expected 'PONG', got: 'Ping' |
| `command-r-plus` | text | ❌ `empty` | 0.39s | Empty response |
| `command-r7b-arabic-02-2025` | text | ❌ `timeout` | 64.71s | Timeout limit exceeded |

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

