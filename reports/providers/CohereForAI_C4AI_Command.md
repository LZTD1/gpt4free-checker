# CohereForAI_C4AI_Command

- **Label:** CohereForAI C4AI Command
- **URL:** https://coherelabs-c4ai-command.hf.space
- **Models:** 7
- **Working tests:** 4 / 7
- **Avg response time:** 3.10s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `command-a-03-2025` | text | ✅ `ok` | 4.68s | contains expected token 'PONG' |
| `command-r-plus-08-2024` | text | ✅ `ok` | 3.14s | contains expected token 'PONG' |
| `command-r7b-12-2024` | text | ✅ `ok` | 2.72s | contains expected token 'PONG' |
| `command-r7b-arabic-02-2025` | text | ✅ `ok` | 1.87s | contains expected token 'PONG' |
| `command-r` | text | ❌ `empty` | 3.29s | Empty response |
| `command-r-08-2024` | text | ❌ `invalid` | 2.79s | expected 'PONG', got: 'Ping' |
| `command-r-plus` | text | ❌ `empty` | 3.67s | Empty response |

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

