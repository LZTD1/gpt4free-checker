# CohereForAI_C4AI_Command

- **Label:** CohereForAI C4AI Command
- **URL:** https://coherelabs-c4ai-command.hf.space
- **Models:** 7
- **Working tests:** 3 / 7
- **Avg response time:** 22.03s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `command-r-plus-08-2024` | text | ✅ `ok` | 42.41s | contains expected token 'PONG' |
| `command-r7b-12-2024` | text | ✅ `ok` | 1.39s | contains expected token 'PONG' |
| `command-r7b-arabic-02-2025` | text | ✅ `ok` | 22.28s | contains expected token 'PONG' |
| `command-a-03-2025` | text | ❌ `timeout` | 63.38s | Timeout limit exceeded |
| `command-r` | text | ❌ `empty` | 42.75s | Empty response |
| `command-r-08-2024` | text | ❌ `timeout` | 45.00s | Timeout limit exceeded |
| `command-r-plus` | text | ❌ `empty` | 22.03s | Empty response |

## Sample successful responses

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

