# Perplexity

- **Label:** Perplexity
- **URL:** https://www.perplexity.ai
- **Models:** 46
- **Working tests:** 9 / 11
- **Avg response time:** 1.58s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `claude40opusthinking_labs` | text | ✅ `ok` | 1.80s | contains expected token 'PONG' |
| `experimental` | text | ✅ `ok` | 1.62s | contains expected token 'PONG' |
| `gpt5` | text | ✅ `ok` | 1.46s | contains expected token 'PONG' |
| `grok` | text | ✅ `ok` | 1.47s | contains expected token 'PONG' |
| `o3_labs` | text | ✅ `ok` | 1.55s | contains expected token 'PONG' |
| `o3pro_labs` | text | ✅ `ok` | 1.37s | contains expected token 'PONG' |
| `o3pro_research` | text | ✅ `ok` | 1.89s | contains expected token 'PONG' |
| `pplx_alpha` | text | ✅ `ok` | 1.66s | contains expected token 'PONG' |
| `pplx_pro` | text | ✅ `ok` | 1.41s | contains expected token 'PONG' |
| `gpt5_thinking` | text | ❌ `api_error` | 9.70s | RateLimitError: Response 429: {'status': 'failed', 'error_code': 'RATE_LIMITED', '_response_type': 'RATE_LIMITED', 'text': 'Query rate limit exceeded. Please tr |
| `o1` | text | ❌ `api_error` | 10.41s | RateLimitError: Response 429: {'status': 'failed', 'error_code': 'RATE_LIMITED', '_response_type': 'RATE_LIMITED', 'text': 'Query rate limit exceeded. Please tr |

## Sample successful responses

### `o3_labs` — text

```
PONG
```

### `o3pro_research` — text

```
PONG
```

### `experimental` — text

```
PONG
```

### `grok` — text

```
PONG
```

### `pplx_pro` — text

```
PONG
```

### `pplx_alpha` — text

```
PONG
```

### `gpt5` — text

```
PONG
```

### `o3pro_labs` — text

```
PONG
```

### `claude40opusthinking_labs` — text

```
PONG
```

