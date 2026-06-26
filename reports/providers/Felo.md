# Felo

- **Label:** Felo
- **URL:** https://felo.ai
- **Models:** 5
- **Working tests:** 2 / 5
- **Avg response time:** 4.19s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `felo-chat` | text | ✅ `ok` | 2.15s | contains expected token 'PONG' |
| `felo-document` | text | ✅ `ok` | 6.23s | contains expected token 'PONG' |
| `felo-scholar` | text | ❌ `rate_limited` | 0.22s | RateLimitError: Response 429: {'detail': 'Rate limit exceeded.'} |
| `felo-search` | text | ❌ `exception` | 5.40s | TypeError: sequence item 2: expected str instance, Sources found |
| `felo-social` | text | ❌ `exception` | 5.81s | TypeError: sequence item 2: expected str instance, Sources found |

## Sample successful responses

### `felo-chat` — text

```
PONG
```

### `felo-document` — text

```
PONG
```

