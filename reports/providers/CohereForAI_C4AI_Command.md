# CohereForAI_C4AI_Command

- **Label:** CohereForAI C4AI Command
- **URL:** https://coherelabs-c4ai-command.hf.space
- **Models:** 7
- **Working tests:** 3 / 7
- **Avg response time:** 1.48s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `command-r-plus-08-2024` | text | ✅ `ok` | 2.08s | contains expected token 'PONG' |
| `command-r7b-12-2024` | text | ✅ `ok` | 1.34s | contains expected token 'PONG' |
| `command-r7b-arabic-02-2025` | text | ✅ `ok` | 1.02s | contains expected token 'PONG' |
| `command-a-03-2025` | text | ❌ `timeout` | 26.01s | Timeout limit exceeded |
| `command-r` | text | ❌ `empty` | 0.23s | Empty response |
| `command-r-08-2024` | text | ❌ `invalid` | 0.34s | expected 'PONG', got: 'Ping' |
| `command-r-plus` | text | ❌ `empty` | 0.22s | Empty response |

## Sample successful responses

### `command-r7b-arabic-02-2025` — text

```
PONG
```

### `command-r7b-12-2024` — text

```
PONG
```

### `command-r-plus-08-2024` — text

```
PONG
```

