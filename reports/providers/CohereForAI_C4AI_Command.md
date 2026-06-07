# CohereForAI_C4AI_Command

- **Label:** CohereForAI C4AI Command
- **URL:** https://coherelabs-c4ai-command.hf.space
- **Models:** 7
- **Working tests:** 3 / 7
- **Avg response time:** 0.46s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `command-r-plus-08-2024` | text | ✅ `ok` | 0.39s | contains expected token 'PONG' |
| `command-r7b-12-2024` | text | ✅ `ok` | 0.45s | contains expected token 'PONG' |
| `command-r7b-arabic-02-2025` | text | ✅ `ok` | 0.52s | contains expected token 'PONG' |
| `command-a-03-2025` | text | ❌ `invalid` | 0.25s | expected 'PONG', got: 'PING' |
| `command-r` | text | ❌ `empty` | 0.81s | Empty response |
| `command-r-08-2024` | text | ❌ `invalid` | 0.45s | expected 'PONG', got: 'Ping' |
| `command-r-plus` | text | ❌ `empty` | 0.61s | Empty response |

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

