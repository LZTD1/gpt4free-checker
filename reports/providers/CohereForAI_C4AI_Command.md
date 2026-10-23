# CohereForAI_C4AI_Command

- **Label:** CohereForAI C4AI Command
- **URL:** https://coherelabs-c4ai-command.hf.space
- **Models:** 7
- **Working tests:** 3 / 7
- **Avg response time:** 22.52s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `command-a-03-2025` | text | ✅ `ok` | 21.03s | contains expected token 'PONG' |
| `command-r-plus-08-2024` | text | ✅ `ok` | 22.54s | contains expected token 'PONG' |
| `command-r7b-12-2024` | text | ✅ `ok` | 23.98s | contains expected token 'PONG' |
| `command-r` | text | ❌ `empty` | 44.51s | Empty response |
| `command-r-08-2024` | text | ❌ `timeout` | 64.87s | Timeout limit exceeded |
| `command-r-plus` | text | ❌ `empty` | 22.50s | Empty response |
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

