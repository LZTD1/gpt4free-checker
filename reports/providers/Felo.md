# Felo

- **Label:** Felo
- **URL:** https://felo.ai
- **Models:** 5
- **Working tests:** 2 / 5
- **Avg response time:** 5.82s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `felo-chat` | text | ✅ `ok` | 1.95s | contains expected token 'PONG' |
| `felo-document` | text | ✅ `ok` | 9.69s | contains expected token 'PONG' |
| `felo-scholar` | text | ❌ `rate_limited` | 0.22s | RateLimitError: Response 429: {'detail': 'Rate limit exceeded.'} |
| `felo-search` | text | ❌ `exception` | 5.03s | TypeError: sequence item 2: expected str instance, Sources found |
| `felo-social` | text | ❌ `exception` | 4.52s | TypeError: sequence item 2: expected str instance, Sources found |

## Sample successful responses

### `felo-chat` — text

```
PONG
```

### `felo-document` — text

```
PONG
```

