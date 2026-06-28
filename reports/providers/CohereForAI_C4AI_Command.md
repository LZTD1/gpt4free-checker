# CohereForAI_C4AI_Command

- **Label:** CohereForAI C4AI Command
- **URL:** https://coherelabs-c4ai-command.hf.space
- **Models:** 7
- **Working tests:** 3 / 7
- **Avg response time:** 1.55s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `command-r-plus-08-2024` | text | ✅ `ok` | 1.64s | contains expected token 'PONG' |
| `command-r7b-12-2024` | text | ✅ `ok` | 1.71s | contains expected token 'PONG' |
| `command-r7b-arabic-02-2025` | text | ✅ `ok` | 1.29s | contains expected token 'PONG' |
| `command-a-03-2025` | text | ❌ `invalid` | 3.47s | expected 'PONG', got: 'PING' |
| `command-r` | text | ❌ `empty` | 4.76s | Empty response |
| `command-r-08-2024` | text | ❌ `invalid` | 0.72s | expected 'PONG', got: 'Ping' |
| `command-r-plus` | text | ❌ `empty` | 3.00s | Empty response |

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

