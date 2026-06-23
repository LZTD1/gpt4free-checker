# Felo

- **Label:** Felo
- **URL:** https://felo.ai
- **Models:** 5
- **Working tests:** 2 / 5
- **Avg response time:** 3.81s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `felo-chat` | text | ✅ `ok` | 1.80s | contains expected token 'PONG' |
| `felo-document` | text | ✅ `ok` | 5.81s | contains expected token 'PONG' |
| `felo-scholar` | text | ❌ `rate_limited` | 0.19s | RateLimitError: Response 429: {'detail': 'Rate limit exceeded.'} |
| `felo-search` | text | ❌ `exception` | 6.47s | TypeError: sequence item 2: expected str instance, Sources found |
| `felo-social` | text | ❌ `exception` | 5.98s | TypeError: sequence item 2: expected str instance, Sources found |

## Sample successful responses

### `felo-chat` — text

```
PONG
```

### `felo-document` — text

```
PONG
```

