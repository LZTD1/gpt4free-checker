# CohereForAI_C4AI_Command

- **Label:** CohereForAI C4AI Command
- **URL:** https://coherelabs-c4ai-command.hf.space
- **Models:** 7
- **Working tests:** 3 / 7
- **Avg response time:** 0.59s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `command-a-03-2025` | text | ✅ `ok` | 0.66s | contains expected token 'PONG' |
| `command-r-plus-08-2024` | text | ✅ `ok` | 0.64s | contains expected token 'PONG' |
| `command-r7b-12-2024` | text | ✅ `ok` | 0.46s | contains expected token 'PONG' |
| `command-r` | text | ❌ `empty` | 0.34s | Empty response |
| `command-r-08-2024` | text | ❌ `invalid` | 0.52s | expected 'PONG', got: 'Ping' |
| `command-r-plus` | text | ❌ `empty` | 0.31s | Empty response |
| `command-r7b-arabic-02-2025` | text | ❌ `timeout` | 64.95s | Timeout limit exceeded |

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

