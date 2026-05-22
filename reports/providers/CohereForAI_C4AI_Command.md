# CohereForAI_C4AI_Command

- **Label:** CohereForAI C4AI Command
- **URL:** https://coherelabs-c4ai-command.hf.space
- **Models:** 7
- **Working tests:** 4 / 7
- **Avg response time:** 2.86s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `command-a-03-2025` | text | ✅ `ok` | 5.67s | contains expected token 'PONG' |
| `command-r-plus-08-2024` | text | ✅ `ok` | 1.98s | contains expected token 'PONG' |
| `command-r7b-12-2024` | text | ✅ `ok` | 2.01s | contains expected token 'PONG' |
| `command-r7b-arabic-02-2025` | text | ✅ `ok` | 1.76s | contains expected token 'PONG' |
| `command-r` | text | ❌ `empty` | 4.38s | Empty response |
| `command-r-08-2024` | text | ❌ `invalid` | 2.92s | expected 'PONG', got: 'Ping' |
| `command-r-plus` | text | ❌ `empty` | 3.43s | Empty response |

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

### `command-a-03-2025` — text

```
PONG
```

