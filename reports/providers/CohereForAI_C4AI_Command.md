# CohereForAI_C4AI_Command

- **Label:** CohereForAI C4AI Command
- **URL:** https://coherelabs-c4ai-command.hf.space
- **Models:** 7
- **Working tests:** 4 / 7
- **Avg response time:** 32.33s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `command-a-03-2025` | text | ✅ `ok` | 22.80s | contains expected token 'PONG' |
| `command-r-plus-08-2024` | text | ✅ `ok` | 22.60s | contains expected token 'PONG' |
| `command-r7b-12-2024` | text | ✅ `ok` | 41.32s | contains expected token 'PONG' |
| `command-r7b-arabic-02-2025` | text | ✅ `ok` | 42.60s | contains expected token 'PONG' |
| `command-r` | text | ❌ `timeout` | 63.23s | Timeout limit exceeded |
| `command-r-08-2024` | text | ❌ `invalid` | 0.69s | expected 'PONG', got: 'Ping' |
| `command-r-plus` | text | ❌ `empty` | 44.50s | Empty response |

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

