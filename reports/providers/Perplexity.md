# Perplexity

- **Label:** Perplexity
- **URL:** https://www.perplexity.ai
- **Models:** 46
- **Working tests:** 1 / 46
- **Avg response time:** 1.96s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `claude45sonnet` | text | ✅ `ok` | 1.96s | contains expected token 'PONG' |
| `auto` | text | ❌ `invalid` | 7.91s | expected 'PONG', got: 'Sign up and repeat your request.' |
| `claude2` | text | ❌ `invalid` | 7.95s | expected 'PONG', got: 'Sign up and repeat your request.' |
| `claude35haiku` | text | ❌ `empty` | 0.20s | Empty response |
| `claude37sonnetthinking` | text | ❌ `invalid` | 7.96s | expected 'PONG', got: 'Sign up and repeat your request.' |
| `claude3opus` | text | ❌ `empty` | 0.40s | Empty response |
| `claude40opus` | text | ❌ `invalid` | 7.78s | expected 'PONG', got: 'Sign up and repeat your request.' |
| `claude40opus_research` | text | ❌ `invalid` | 7.88s | expected 'PONG', got: 'Sign up and repeat your request.' |
| `claude40opusthinking` | text | ❌ `invalid` | 7.84s | expected 'PONG', got: 'Sign up and repeat your request.' |
| `claude40opusthinking_labs` | text | ❌ `invalid` | 8.22s | expected 'PONG', got: 'Sign up and repeat your request.' |
| `claude40opusthinking_research` | text | ❌ `invalid` | 7.78s | expected 'PONG', got: 'Sign up and repeat your request.' |
| `claude40sonnet_research` | text | ❌ `invalid` | 8.00s | expected 'PONG', got: 'Sign up and repeat your request.' |
| `claude40sonnetthinking_labs` | text | ❌ `invalid` | 7.80s | expected 'PONG', got: 'Sign up and repeat your request.' |
| `claude40sonnetthinking_research` | text | ❌ `invalid` | 8.42s | expected 'PONG', got: 'Sign up and repeat your request.' |
| `claude41opusthinking` | text | ❌ `invalid` | 7.77s | expected 'PONG', got: 'Sign up and repeat your request.' |
| `claude45sonnetthinking` | text | ❌ `invalid` | 8.44s | expected 'PONG', got: 'Sign up and repeat your request.' |
| `comet_max_assistant` | text | ❌ `invalid` | 7.84s | expected 'PONG', got: 'Sign up and repeat your request.' |
| `experimental` | text | ❌ `invalid` | 7.88s | expected 'PONG', got: 'Sign up and repeat your request.' |
| `gemini` | text | ❌ `rate_limited` | 0.19s | RateLimitError: Response 429: {'status': 'failed', 'error_code': 'RATE_LIMITED', '_response_type': 'RATE_LIMITED', 'text': 'Query rate limit exceeded. Please tr |
| `gemini2flash` | text | ❌ `invalid` | 8.03s | expected 'PONG', got: 'Sign up and repeat your request.' |
| `gpt4` | text | ❌ `invalid` | 8.01s | expected 'PONG', got: 'Sign up and repeat your request.' |
| `gpt41` | text | ❌ `invalid` | 7.98s | expected 'PONG', got: 'Sign up and repeat your request.' |
| `gpt45` | text | ❌ `invalid` | 7.92s | expected 'PONG', got: 'Sign up and repeat your request.' |
| `gpt4o` | text | ❌ `invalid` | 7.70s | expected 'PONG', got: 'Sign up and repeat your request.' |
| `gpt5` | text | ❌ `invalid` | 7.99s | expected 'PONG', got: 'Sign up and repeat your request.' |
| `gpt5_thinking` | text | ❌ `invalid` | 7.69s | expected 'PONG', got: 'Sign up and repeat your request.' |
| `grok` | text | ❌ `invalid` | 7.85s | expected 'PONG', got: 'Sign up and repeat your request.' |
| `grok4` | text | ❌ `invalid` | 7.82s | expected 'PONG', got: 'Sign up and repeat your request.' |
| `llama_x_large` | text | ❌ `empty` | 0.22s | Empty response |
| `mistral` | text | ❌ `empty` | 0.20s | Empty response |
| `o1` | text | ❌ `empty` | 0.21s | Empty response |
| `o3` | text | ❌ `invalid` | 7.66s | expected 'PONG', got: 'Sign up and repeat your request.' |
| `o3_labs` | text | ❌ `invalid` | 8.23s | expected 'PONG', got: 'Sign up and repeat your request.' |
| `o3_research` | text | ❌ `invalid` | 7.69s | expected 'PONG', got: 'Sign up and repeat your request.' |
| `o3mini` | text | ❌ `invalid` | 7.86s | expected 'PONG', got: 'Sign up and repeat your request.' |
| `o3pro` | text | ❌ `invalid` | 7.79s | expected 'PONG', got: 'Sign up and repeat your request.' |
| `o3pro_labs` | text | ❌ `invalid` | 7.71s | expected 'PONG', got: 'Sign up and repeat your request.' |
| `o3pro_research` | text | ❌ `invalid` | 7.84s | expected 'PONG', got: 'Sign up and repeat your request.' |
| `o4mini` | text | ❌ `invalid` | 8.04s | expected 'PONG', got: 'Sign up and repeat your request.' |
| `pplx_alpha` | text | ❌ `invalid` | 7.73s | expected 'PONG', got: 'Sign up and repeat your request.' |
| `pplx_beta` | text | ❌ `invalid` | 8.12s | expected 'PONG', got: 'Sign up and repeat your request.' |
| `pplx_pro` | text | ❌ `invalid` | 8.17s | expected 'PONG', got: 'Sign up and repeat your request.' |
| `pplx_pro_upgraded` | text | ❌ `invalid` | 8.06s | expected 'PONG', got: 'Sign up and repeat your request.' |
| `pplx_reasoning` | text | ❌ `invalid` | 7.96s | expected 'PONG', got: 'Sign up and repeat your request.' |
| `r1` | text | ❌ `invalid` | 7.84s | expected 'PONG', got: 'Sign up and repeat your request.' |
| `turbo` | text | ❌ `invalid` | 7.88s | expected 'PONG', got: 'Sign up and repeat your request.' |

## Sample successful responses

### `claude45sonnet` — text

```
PONG
```

