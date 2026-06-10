# CohereForAI_C4AI_Command

- **Label:** CohereForAI C4AI Command
- **URL:** https://coherelabs-c4ai-command.hf.space
- **Models:** 7
- **Working tests:** 3 / 7
- **Avg response time:** 0.27s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `command-r-plus-08-2024` | text | ✅ `ok` | 0.30s | contains expected token 'PONG' |
| `command-r7b-12-2024` | text | ✅ `ok` | 0.27s | contains expected token 'PONG' |
| `command-r7b-arabic-02-2025` | text | ✅ `ok` | 0.25s | contains expected token 'PONG' |
| `command-a-03-2025` | text | ❌ `invalid` | 2.75s | expected 'PONG', got: 'PING' |
| `command-r` | text | ❌ `empty` | 0.11s | Empty response |
| `command-r-08-2024` | text | ❌ `invalid` | 0.21s | expected 'PONG', got: 'Ping' |
| `command-r-plus` | text | ❌ `empty` | 0.12s | Empty response |

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

