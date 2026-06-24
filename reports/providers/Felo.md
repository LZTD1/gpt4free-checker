# Felo

- **Label:** Felo
- **URL:** https://felo.ai
- **Models:** 5
- **Working tests:** 2 / 5
- **Avg response time:** 4.66s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `felo-chat` | text | ✅ `ok` | 2.52s | contains expected token 'PONG' |
| `felo-document` | text | ✅ `ok` | 6.81s | contains expected token 'PONG' |
| `felo-scholar` | text | ❌ `exception` | 12.56s | TypeError: sequence item 2: expected str instance, Sources found |
| `felo-search` | text | ❌ `exception` | 8.48s | TypeError: sequence item 2: expected str instance, Sources found |
| `felo-social` | text | ❌ `exception` | 5.82s | TypeError: sequence item 2: expected str instance, Sources found |

## Sample successful responses

### `felo-chat` — text

```
PONG
```

### `felo-document` — text

```
PONG
```

