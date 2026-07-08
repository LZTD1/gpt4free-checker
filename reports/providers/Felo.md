# Felo

- **Label:** Felo
- **URL:** https://felo.ai
- **Models:** 5
- **Working tests:** 3 / 5
- **Avg response time:** 5.51s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `felo-chat` | text | ✅ `ok` | 2.28s | contains expected token 'PONG' |
| `felo-document` | text | ✅ `ok` | 4.12s | contains expected token 'PONG' |
| `felo-scholar` | text | ✅ `ok` | 10.14s | contains expected token 'PONG' |
| `felo-search` | text | ❌ `exception` | 4.88s | TypeError: sequence item 2: expected str instance, Sources found |
| `felo-social` | text | ❌ `rate_limited` | 0.23s | RateLimitError: Response 429: {'detail': 'Rate limit exceeded.'} |

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

