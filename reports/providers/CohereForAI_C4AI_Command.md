# CohereForAI_C4AI_Command

- **Label:** CohereForAI C4AI Command
- **URL:** https://coherelabs-c4ai-command.hf.space
- **Models:** 7
- **Working tests:** 4 / 7
- **Avg response time:** 16.48s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `command-a-03-2025` | text | ✅ `ok` | 1.01s | contains expected token 'PONG' |
| `command-r-plus-08-2024` | text | ✅ `ok` | 21.03s | contains expected token 'PONG' |
| `command-r7b-12-2024` | text | ✅ `ok` | 21.88s | contains expected token 'PONG' |
| `command-r7b-arabic-02-2025` | text | ✅ `ok` | 22.03s | contains expected token 'PONG' |
| `command-r` | text | ❌ `empty` | 41.18s | Empty response |
| `command-r-08-2024` | text | ❌ `invalid` | 21.65s | expected 'PONG', got: 'Ping' |
| `command-r-plus` | text | ❌ `empty` | 1.74s | Empty response |

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

