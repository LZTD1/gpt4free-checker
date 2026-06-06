# Perplexity

- **Label:** Perplexity
- **URL:** https://www.perplexity.ai
- **Models:** 46
- **Working tests:** 9 / 11
- **Avg response time:** 2.57s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `claude40opusthinking` | text | ✅ `ok` | 2.83s | contains expected token 'PONG' |
| `claude40sonnetthinking_research` | text | ✅ `ok` | 3.19s | contains expected token 'PONG' |
| `claude45sonnetthinking` | text | ✅ `ok` | 2.91s | contains expected token 'PONG' |
| `experimental` | text | ✅ `ok` | 3.07s | contains expected token 'PONG' |
| `gpt5` | text | ✅ `ok` | 2.57s | contains expected token 'PONG' |
| `grok` | text | ✅ `ok` | 2.83s | contains expected token 'PONG' |
| `o3_labs` | text | ✅ `ok` | 1.46s | contains expected token 'PONG' |
| `o3_research` | text | ✅ `ok` | 2.97s | contains expected token 'PONG' |
| `o3pro_labs` | text | ✅ `ok` | 1.33s | contains expected token 'PONG' |
| `gemini` | text | ❌ `api_error` | 11.27s | RateLimitError: Response 429: <!DOCTYPE html><html lang="en-US"><head><title>Just a moment...</title><meta http-equiv="Content-Type" content="text/html; charset |
| `o1` | text | ❌ `api_error` | 11.39s | RateLimitError: Response 429: <!DOCTYPE html><html lang="en-US"><head><title>Just a moment...</title><meta http-equiv="Content-Type" content="text/html; charset |

## Sample successful responses

### `o3_labs` — text

```
PONG
```

### `grok` — text

```
PONG
```

### `claude40sonnetthinking_research` — text

```
PONG
```

### `claude40opusthinking` — text

```
PONG
```

### `claude45sonnetthinking` — text

```
PONG
```

### `experimental` — text

```
PONG
```

### `o3_research` — text

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

