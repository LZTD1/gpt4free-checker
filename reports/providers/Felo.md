# Felo

- **Label:** Felo
- **URL:** https://felo.ai
- **Models:** 5
- **Working tests:** 3 / 5
- **Avg response time:** 5.55s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `felo-chat` | text | ✅ `ok` | 2.05s | contains expected token 'PONG' |
| `felo-document` | text | ✅ `ok` | 3.72s | contains expected token 'PONG' |
| `felo-scholar` | text | ✅ `ok` | 10.88s | contains expected token 'PONG' |
| `felo-search` | text | ❌ `exception` | 5.12s | TypeError: sequence item 2: expected str instance, Sources found |
| `felo-social` | text | ❌ `rate_limited` | 0.24s | RateLimitError: Response 429: {'detail': 'Rate limit exceeded.'} |

## Sample successful responses

### `felo-chat` — text

```
PONG
```

### `felo-scholar` — text

```
PONG
```

### `felo-document` — text

```
PONG
```

