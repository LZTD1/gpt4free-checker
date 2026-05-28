# CohereForAI_C4AI_Command

- **Label:** CohereForAI C4AI Command
- **URL:** https://coherelabs-c4ai-command.hf.space
- **Models:** 7
- **Working tests:** 4 / 7
- **Avg response time:** 0.86s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `command-a-03-2025` | text | ✅ `ok` | 1.05s | contains expected token 'PONG' |
| `command-r-plus-08-2024` | text | ✅ `ok` | 1.10s | contains expected token 'PONG' |
| `command-r7b-12-2024` | text | ✅ `ok` | 0.55s | contains expected token 'PONG' |
| `command-r7b-arabic-02-2025` | text | ✅ `ok` | 0.74s | contains expected token 'PONG' |
| `command-r` | text | ❌ `empty` | 0.74s | Empty response |
| `command-r-08-2024` | text | ❌ `invalid` | 0.32s | expected 'PONG', got: 'Ping' |
| `command-r-plus` | text | ❌ `empty` | 0.47s | Empty response |

## Sample successful responses

### `command-r7b-12-2024` — text

```
PONG
```

### `command-r7b-arabic-02-2025` — text

```
PONG
```

### `command-a-03-2025` — text

```
PONG
```

### `command-r-plus-08-2024` — text

```
PONG
```

