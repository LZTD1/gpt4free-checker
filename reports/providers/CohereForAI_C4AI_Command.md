# CohereForAI_C4AI_Command

- **Label:** CohereForAI C4AI Command
- **URL:** https://coherelabs-c4ai-command.hf.space
- **Models:** 7
- **Working tests:** 3 / 7
- **Avg response time:** 2.33s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `command-r-plus-08-2024` | text | ✅ `ok` | 1.06s | contains expected token 'PONG' |
| `command-r7b-12-2024` | text | ✅ `ok` | 3.16s | contains expected token 'PONG' |
| `command-r7b-arabic-02-2025` | text | ✅ `ok` | 2.76s | contains expected token 'PONG' |
| `command-a-03-2025` | text | ❌ `invalid` | 0.67s | expected 'PONG', got: 'PING' |
| `command-r` | text | ❌ `empty` | 4.66s | Empty response |
| `command-r-08-2024` | text | ❌ `invalid` | 4.42s | expected 'PONG', got: 'Ping' |
| `command-r-plus` | text | ❌ `empty` | 1.31s | Empty response |

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

