# CohereForAI_C4AI_Command

- **Label:** CohereForAI C4AI Command
- **URL:** https://coherelabs-c4ai-command.hf.space
- **Models:** 7
- **Working tests:** 3 / 7
- **Avg response time:** 36.27s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `command-a-03-2025` | text | ✅ `ok` | 43.05s | contains expected token 'PONG' |
| `command-r7b-12-2024` | text | ✅ `ok` | 43.75s | contains expected token 'PONG' |
| `command-r7b-arabic-02-2025` | text | ✅ `ok` | 22.02s | contains expected token 'PONG' |
| `command-r` | text | ❌ `empty` | 44.16s | Empty response |
| `command-r-08-2024` | text | ❌ `invalid` | 41.55s | expected 'PONG', got: 'Ping' |
| `command-r-plus` | text | ❌ `empty` | 43.66s | Empty response |
| `command-r-plus-08-2024` | text | ❌ `timeout` | 63.23s | Timeout limit exceeded |

## Sample successful responses

### `command-a-03-2025` — text

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

