# CohereForAI_C4AI_Command

- **Label:** CohereForAI C4AI Command
- **URL:** https://coherelabs-c4ai-command.hf.space
- **Models:** 7
- **Working tests:** 4 / 7
- **Avg response time:** 43.46s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `command-a-03-2025` | text | ✅ `ok` | 44.00s | contains expected token 'PONG' |
| `command-r-plus-08-2024` | text | ✅ `ok` | 44.03s | contains expected token 'PONG' |
| `command-r7b-12-2024` | text | ✅ `ok` | 43.08s | contains expected token 'PONG' |
| `command-r7b-arabic-02-2025` | text | ✅ `ok` | 42.73s | contains expected token 'PONG' |
| `command-r` | text | ❌ `timeout` | 63.16s | Timeout limit exceeded |
| `command-r-08-2024` | text | ❌ `invalid` | 23.00s | expected 'PONG', got: 'Ping' |
| `command-r-plus` | text | ❌ `timeout` | 45.00s | Timeout limit exceeded |

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

### `command-r7b-arabic-02-2025` — text

```
PONG
```

