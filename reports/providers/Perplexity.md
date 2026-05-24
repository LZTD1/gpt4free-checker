# Perplexity

- **Label:** Perplexity
- **URL:** https://www.perplexity.ai
- **Models:** 46
- **Working tests:** 10 / 18
- **Avg response time:** 1.46s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `claude40opusthinking_labs` | text | ✅ `ok` | 1.33s | contains expected token 'PONG' |
| `claude40sonnetthinking_research` | text | ✅ `ok` | 1.21s | contains expected token 'PONG' |
| `claude41opusthinking` | text | ✅ `ok` | 1.46s | contains expected token 'PONG' |
| `claude45sonnet` | text | ✅ `ok` | 1.71s | contains expected token 'PONG' |
| `claude45sonnetthinking` | text | ✅ `ok` | 1.22s | contains expected token 'PONG' |
| `gemini2flash` | text | ✅ `ok` | 1.16s | contains expected token 'PONG' |
| `o3pro_research` | text | ✅ `ok` | 1.73s | contains expected token 'PONG' |
| `pplx_pro` | text | ✅ `ok` | 1.68s | contains expected token 'PONG' |
| `pplx_reasoning` | text | ✅ `ok` | 1.72s | contains expected token 'PONG' |
| `r1` | text | ✅ `ok` | 1.36s | contains expected token 'PONG' |
| `claude35haiku` | text | ❌ `api_error` | 8.77s | RateLimitError: Response 429: {'status': 'failed', 'error_code': 'RATE_LIMITED', '_response_type': 'RATE_LIMITED', 'text': 'Query rate limit exceeded. Please tr |
| `claude40sonnet_research` | text | ❌ `exception` | 2.47s | CloudflareError: Response 403: Cloudflare detected |
| `llama_x_large` | text | ❌ `exception` | 9.84s | CloudflareError: Response 403: Cloudflare detected |
| `mistral` | text | ❌ `exception` | 0.94s | CloudflareError: Response 403: Cloudflare detected |
| `o1` | text | ❌ `exception` | 1.21s | CloudflareError: Response 403: Cloudflare detected |
| `o3pro_labs` | text | ❌ `exception` | 2.06s | CloudflareError: Response 403: Cloudflare detected |
| `pplx_alpha` | text | ❌ `api_error` | 0.97s | RateLimitError: Response 429: {'status': 'failed', 'error_code': 'RATE_LIMITED', '_response_type': 'RATE_LIMITED', 'text': 'Query rate limit exceeded. Please tr |
| `pplx_pro_upgraded` | text | ❌ `exception` | 1.11s | CloudflareError: Response 403: Cloudflare detected |

## Sample successful responses

### `claude45sonnetthinking` — text

```
PONG
```

### `r1` — text

```
PONG
```

### `claude40opusthinking_labs` — text

```
PONG
```

### `claude45sonnet` — text

```
PONG
```

### `claude40sonnetthinking_research` — text

```
PONG
```

### `o3pro_research` — text

```
PONG
```

### `pplx_reasoning` — text

```
PONG
```

### `gemini2flash` — text

```
PONG
```

### `claude41opusthinking` — text

```
PONG
```

### `pplx_pro` — text

```
PONG
```

