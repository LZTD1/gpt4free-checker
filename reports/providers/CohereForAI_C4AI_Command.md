# CohereForAI_C4AI_Command

- **Label:** CohereForAI C4AI Command
- **URL:** https://coherelabs-c4ai-command.hf.space
- **Models:** 7
- **Working tests:** 4 / 7
- **Avg response time:** 4.99s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `command-a-03-2025` | text | ✅ `ok` | 8.17s | contains expected token 'PONG' |
| `command-r-plus-08-2024` | text | ✅ `ok` | 5.93s | contains expected token 'PONG' |
| `command-r7b-12-2024` | text | ✅ `ok` | 2.96s | contains expected token 'PONG' |
| `command-r7b-arabic-02-2025` | text | ✅ `ok` | 2.90s | contains expected token 'PONG' |
| `command-r` | text | ❌ `empty` | 4.06s | Empty response |
| `command-r-08-2024` | text | ❌ `exception` | 5.76s | ResponseStatusError: Response 500: HTML content |
| `command-r-plus` | text | ❌ `empty` | 9.89s | Empty response |

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

