# CohereForAI_C4AI_Command

- **Label:** CohereForAI C4AI Command
- **URL:** https://coherelabs-c4ai-command.hf.space
- **Models:** 7
- **Working tests:** 4 / 7
- **Avg response time:** 11.23s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `command-a-03-2025` | text | ✅ `ok` | 21.41s | contains expected token 'PONG' |
| `command-r-plus-08-2024` | text | ✅ `ok` | 21.03s | contains expected token 'PONG' |
| `command-r7b-12-2024` | text | ✅ `ok` | 0.52s | contains expected token 'PONG' |
| `command-r7b-arabic-02-2025` | text | ✅ `ok` | 1.96s | contains expected token 'PONG' |
| `command-r` | text | ❌ `empty` | 43.46s | Empty response |
| `command-r-08-2024` | text | ❌ `timeout` | 45.00s | Timeout limit exceeded |
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

