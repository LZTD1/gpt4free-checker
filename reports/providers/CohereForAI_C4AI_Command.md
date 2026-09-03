# CohereForAI_C4AI_Command

- **Label:** CohereForAI C4AI Command
- **URL:** https://coherelabs-c4ai-command.hf.space
- **Models:** 7
- **Working tests:** 3 / 7
- **Avg response time:** 43.93s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `command-a-03-2025` | text | ✅ `ok` | 44.37s | contains expected token 'PONG' |
| `command-r-plus-08-2024` | text | ✅ `ok` | 42.94s | contains expected token 'PONG' |
| `command-r7b-12-2024` | text | ✅ `ok` | 44.47s | contains expected token 'PONG' |
| `command-r` | text | ❌ `empty` | 44.14s | Empty response |
| `command-r-08-2024` | text | ❌ `invalid` | 44.17s | expected 'PONG', got: 'Ping' |
| `command-r-plus` | text | ❌ `empty` | 43.85s | Empty response |
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

