# Felo

- **Label:** Felo
- **URL:** https://felo.ai
- **Models:** 5
- **Working tests:** 3 / 5
- **Avg response time:** 5.29s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `felo-chat` | text | ✅ `ok` | 1.78s | contains expected token 'PONG' |
| `felo-document` | text | ✅ `ok` | 4.49s | contains expected token 'PONG' |
| `felo-scholar` | text | ✅ `ok` | 9.61s | contains expected token 'PONG' |
| `felo-search` | text | ❌ `exception` | 7.08s | TypeError: sequence item 2: expected str instance, Sources found |
| `felo-social` | text | ❌ `rate_limited` | 0.40s | RateLimitError: Response 429: {'detail': 'Rate limit exceeded.'} |

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

