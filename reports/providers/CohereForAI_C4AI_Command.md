# CohereForAI_C4AI_Command

- **Label:** CohereForAI C4AI Command
- **URL:** https://coherelabs-c4ai-command.hf.space
- **Models:** 7
- **Working tests:** 3 / 7
- **Avg response time:** 13.89s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `command-r-plus-08-2024` | text | ✅ `ok` | 10.74s | contains expected token 'PONG' |
| `command-r7b-12-2024` | text | ✅ `ok` | 10.77s | contains expected token 'PONG' |
| `command-r7b-arabic-02-2025` | text | ✅ `ok` | 20.17s | contains expected token 'PONG' |
| `command-a-03-2025` | text | ❌ `invalid` | 2.16s | expected 'PONG', got: 'PING' |
| `command-r` | text | ❌ `empty` | 3.41s | Empty response |
| `command-r-08-2024` | text | ❌ `invalid` | 9.89s | expected 'PONG', got: 'Ping' |
| `command-r-plus` | text | ❌ `empty` | 11.66s | Empty response |

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

