# Felo

- **Label:** Felo
- **URL:** https://felo.ai
- **Models:** 5
- **Working tests:** 2 / 5
- **Avg response time:** 21.00s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `felo-chat` | text | ✅ `ok` | 21.03s | contains expected token 'PONG' |
| `felo-document` | text | ✅ `ok` | 20.97s | contains expected token 'PONG' |
| `felo-scholar` | text | ❌ `exception` | 21.03s | TypeError: sequence item 2: expected str instance, Sources found |
| `felo-search` | text | ❌ `exception` | 21.53s | TypeError: sequence item 2: expected str instance, Sources found |
| `felo-social` | text | ❌ `exception` | 22.03s | TypeError: sequence item 2: expected str instance, Sources found |

## Sample successful responses

### `felo-chat` — text

```
PONG
```

### `felo-document` — text

```
PONG
```

