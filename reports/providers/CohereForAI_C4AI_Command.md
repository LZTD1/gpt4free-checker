# CohereForAI_C4AI_Command

- **Label:** CohereForAI C4AI Command
- **URL:** https://coherelabs-c4ai-command.hf.space
- **Models:** 7
- **Working tests:** 4 / 7
- **Avg response time:** 0.46s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `command-a-03-2025` | text | ✅ `ok` | 0.77s | contains expected token 'PONG' |
| `command-r-plus-08-2024` | text | ✅ `ok` | 0.32s | contains expected token 'PONG' |
| `command-r7b-12-2024` | text | ✅ `ok` | 0.39s | contains expected token 'PONG' |
| `command-r7b-arabic-02-2025` | text | ✅ `ok` | 0.37s | contains expected token 'PONG' |
| `command-r` | text | ❌ `empty` | 22.20s | Empty response |
| `command-r-08-2024` | text | ❌ `invalid` | 0.33s | expected 'PONG', got: 'Ping' |
| `command-r-plus` | text | ❌ `empty` | 22.04s | Empty response |

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

