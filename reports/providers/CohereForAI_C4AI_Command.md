# CohereForAI_C4AI_Command

- **Label:** CohereForAI C4AI Command
- **URL:** https://coherelabs-c4ai-command.hf.space
- **Models:** 7
- **Working tests:** 4 / 7
- **Avg response time:** 37.94s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `command-a-03-2025` | text | ✅ `ok` | 22.68s | contains expected token 'PONG' |
| `command-r-plus-08-2024` | text | ✅ `ok` | 42.75s | contains expected token 'PONG' |
| `command-r7b-12-2024` | text | ✅ `ok` | 42.44s | contains expected token 'PONG' |
| `command-r7b-arabic-02-2025` | text | ✅ `ok` | 43.89s | contains expected token 'PONG' |
| `command-r` | text | ❌ `timeout` | 46.64s | Timeout limit exceeded |
| `command-r-08-2024` | text | ❌ `invalid` | 21.80s | expected 'PONG', got: 'Ping' |
| `command-r-plus` | text | ❌ `empty` | 44.27s | Empty response |

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

