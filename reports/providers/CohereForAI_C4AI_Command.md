# CohereForAI_C4AI_Command

- **Label:** CohereForAI C4AI Command
- **URL:** https://coherelabs-c4ai-command.hf.space
- **Models:** 7
- **Working tests:** 2 / 7
- **Avg response time:** 10.78s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `command-r-plus-08-2024` | text | ✅ `ok` | 21.03s | contains expected token 'PONG' |
| `command-r7b-12-2024` | text | ✅ `ok` | 0.54s | contains expected token 'PONG' |
| `command-a-03-2025` | text | ❌ `invalid` | 0.70s | expected 'PONG', got: 'PING' |
| `command-r` | text | ❌ `empty` | 1.58s | Empty response |
| `command-r-08-2024` | text | ❌ `invalid` | 1.96s | expected 'PONG', got: 'Ping' |
| `command-r-plus` | text | ❌ `empty` | 1.35s | Empty response |
| `command-r7b-arabic-02-2025` | text | ❌ `invalid` | 44.73s | expected 'PONG', got: '<PAD><PAD><PAD><PAD><PAD><PAD><PAD><PAD><PAD><PAD><PAD><PAD><PAD><PAD><PAD><PAD>' |

## Sample successful responses

### `command-r-plus-08-2024` — text

```
PONG
```

### `command-r7b-12-2024` — text

```
PONG
```

