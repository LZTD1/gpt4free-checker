# CohereForAI_C4AI_Command

- **Label:** CohereForAI C4AI Command
- **URL:** https://coherelabs-c4ai-command.hf.space
- **Models:** 7
- **Working tests:** 3 / 7
- **Avg response time:** 43.48s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `command-r-plus-08-2024` | text | ✅ `ok` | 43.75s | contains expected token 'PONG' |
| `command-r7b-12-2024` | text | ✅ `ok` | 42.97s | contains expected token 'PONG' |
| `command-r7b-arabic-02-2025` | text | ✅ `ok` | 43.72s | contains expected token 'PONG' |
| `command-a-03-2025` | text | ❌ `invalid` | 43.05s | expected 'PONG', got: 'PING' |
| `command-r` | text | ❌ `empty` | 43.50s | Empty response |
| `command-r-08-2024` | text | ❌ `invalid` | 43.69s | expected 'PONG', got: 'Ping' |
| `command-r-plus` | text | ❌ `empty` | 44.44s | Empty response |

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

