# CohereForAI_C4AI_Command

- **Label:** CohereForAI C4AI Command
- **URL:** https://coherelabs-c4ai-command.hf.space
- **Models:** 7
- **Working tests:** 4 / 7
- **Avg response time:** 3.78s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `command-a-03-2025` | text | ✅ `ok` | 2.67s | contains expected token 'PONG' |
| `command-r-plus-08-2024` | text | ✅ `ok` | 7.25s | contains expected token 'PONG' |
| `command-r7b-12-2024` | text | ✅ `ok` | 3.13s | contains expected token 'PONG' |
| `command-r7b-arabic-02-2025` | text | ✅ `ok` | 2.08s | contains expected token 'PONG' |
| `command-r` | text | ❌ `empty` | 4.50s | Empty response |
| `command-r-08-2024` | text | ❌ `invalid` | 2.99s | expected 'PONG', got: 'Ping' |
| `command-r-plus` | text | ❌ `empty` | 3.58s | Empty response |

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

