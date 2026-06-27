# Felo

- **Label:** Felo
- **URL:** https://felo.ai
- **Models:** 5
- **Working tests:** 4 / 5
- **Avg response time:** 3.30s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `felo-chat` | text | ✅ `ok` | 1.92s | contains expected token 'PONG' |
| `felo-document` | text | ✅ `ok` | 5.88s | contains expected token 'PONG' |
| `felo-search` | text | ✅ `ok` | 2.38s | contains expected token 'PONG' |
| `felo-social` | text | ✅ `ok` | 3.03s | contains expected token 'PONG' |
| `felo-scholar` | text | ❌ `rate_limited` | 0.19s | RateLimitError: Response 429: {'detail': 'Rate limit exceeded.'} |

## Sample successful responses

### `felo-chat` — text

```
PONG
```

### `felo-search` — text

```
PONG
```

### `felo-social` — text

```
PONG
```

### `felo-document` — text

```
PONG
```

