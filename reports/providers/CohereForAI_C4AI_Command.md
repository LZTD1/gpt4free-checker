# CohereForAI_C4AI_Command

- **Label:** CohereForAI C4AI Command
- **URL:** https://coherelabs-c4ai-command.hf.space
- **Models:** 7
- **Working tests:** 3 / 7
- **Avg response time:** 44.18s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `command-a-03-2025` | text | ✅ `ok` | 44.45s | contains expected token 'PONG' |
| `command-r-plus-08-2024` | text | ✅ `ok` | 43.71s | contains expected token 'PONG' |
| `command-r7b-12-2024` | text | ✅ `ok` | 44.38s | contains expected token 'PONG' |
| `command-r` | text | ❌ `timeout` | 64.81s | Timeout limit exceeded |
| `command-r-08-2024` | text | ❌ `invalid` | 21.71s | expected 'PONG', got: 'Ping' |
| `command-r-plus` | text | ❌ `empty` | 43.05s | Empty response |
| `command-r7b-arabic-02-2025` | text | ❌ `timeout` | 64.94s | Timeout limit exceeded |

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

