# Felo

- **Label:** Felo
- **URL:** https://felo.ai
- **Models:** 5
- **Working tests:** 2 / 5
- **Avg response time:** 4.68s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `felo-chat` | text | ✅ `ok` | 2.60s | contains expected token 'PONG' |
| `felo-document` | text | ✅ `ok` | 6.77s | contains expected token 'PONG' |
| `felo-scholar` | text | ❌ `exception` | 10.02s | TypeError: sequence item 2: expected str instance, Sources found |
| `felo-search` | text | ❌ `exception` | 10.44s | TypeError: sequence item 2: expected str instance, Sources found |
| `felo-social` | text | ❌ `exception` | 6.25s | TypeError: sequence item 2: expected str instance, Sources found |

## Sample successful responses

### `felo-chat` — text

```
PONG
```

### `felo-document` — text

```
PONG
```

