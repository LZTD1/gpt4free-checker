# Felo

- **Label:** Felo
- **URL:** https://felo.ai
- **Models:** 5
- **Working tests:** 2 / 5
- **Avg response time:** 6.51s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `felo-chat` | text | ✅ `ok` | 1.93s | contains expected token 'PONG' |
| `felo-document` | text | ✅ `ok` | 11.09s | contains expected token 'PONG' |
| `felo-scholar` | text | ❌ `exception` | 15.28s | TypeError: sequence item 2: expected str instance, Sources found |
| `felo-search` | text | ❌ `exception` | 4.77s | TypeError: sequence item 2: expected str instance, Sources found |
| `felo-social` | text | ❌ `exception` | 3.87s | TypeError: sequence item 2: expected str instance, Sources found |

## Sample successful responses

### `felo-chat` — text

```
PONG
```

### `felo-document` — text

```
PONG
```

