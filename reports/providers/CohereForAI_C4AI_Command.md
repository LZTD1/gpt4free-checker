# CohereForAI_C4AI_Command

- **Label:** CohereForAI C4AI Command
- **URL:** https://coherelabs-c4ai-command.hf.space
- **Models:** 7
- **Working tests:** 3 / 7
- **Avg response time:** 7.87s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `command-a-03-2025` | text | ✅ `ok` | 0.99s | contains expected token 'PONG' |
| `command-r-plus-08-2024` | text | ✅ `ok` | 22.02s | contains expected token 'PONG' |
| `command-r7b-12-2024` | text | ✅ `ok` | 0.60s | contains expected token 'PONG' |
| `command-r` | text | ❌ `empty` | 21.14s | Empty response |
| `command-r-08-2024` | text | ❌ `invalid` | 0.84s | expected 'PONG', got: 'Ping' |
| `command-r-plus` | text | ❌ `empty` | 21.03s | Empty response |
| `command-r7b-arabic-02-2025` | text | ❌ `timeout` | 64.63s | Timeout limit exceeded |

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

