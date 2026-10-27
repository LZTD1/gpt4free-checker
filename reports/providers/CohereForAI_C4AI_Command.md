# CohereForAI_C4AI_Command

- **Label:** CohereForAI C4AI Command
- **URL:** https://coherelabs-c4ai-command.hf.space
- **Models:** 7
- **Working tests:** 3 / 7
- **Avg response time:** 7.30s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `command-r-plus-08-2024` | text | ✅ `ok` | 21.03s | contains expected token 'PONG' |
| `command-r7b-12-2024` | text | ✅ `ok` | 0.44s | contains expected token 'PONG' |
| `command-r7b-arabic-02-2025` | text | ✅ `ok` | 0.43s | contains expected token 'PONG' |
| `command-a-03-2025` | text | ❌ `timeout` | 64.80s | Timeout limit exceeded |
| `command-r` | text | ❌ `empty` | 0.35s | Empty response |
| `command-r-08-2024` | text | ❌ `invalid` | 0.88s | expected 'PONG', got: 'Ping' |
| `command-r-plus` | text | ❌ `empty` | 0.39s | Empty response |

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

