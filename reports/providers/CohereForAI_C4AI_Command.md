# CohereForAI_C4AI_Command

- **Label:** CohereForAI C4AI Command
- **URL:** https://coherelabs-c4ai-command.hf.space
- **Models:** 7
- **Working tests:** 4 / 7
- **Avg response time:** 2.02s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `command-a-03-2025` | text | ✅ `ok` | 1.19s | contains expected token 'PONG' |
| `command-r-plus-08-2024` | text | ✅ `ok` | 2.69s | contains expected token 'PONG' |
| `command-r7b-12-2024` | text | ✅ `ok` | 2.82s | contains expected token 'PONG' |
| `command-r7b-arabic-02-2025` | text | ✅ `ok` | 1.39s | contains expected token 'PONG' |
| `command-r` | text | ❌ `empty` | 0.61s | Empty response |
| `command-r-08-2024` | text | ❌ `invalid` | 0.74s | expected 'PONG', got: 'Ping' |
| `command-r-plus` | text | ❌ `empty` | 1.17s | Empty response |

## Sample successful responses

### `command-r7b-arabic-02-2025` — text

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

### `command-a-03-2025` — text

```
PONG
```

