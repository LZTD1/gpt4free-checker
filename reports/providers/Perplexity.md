# Perplexity

- **Label:** Perplexity
- **URL:** https://www.perplexity.ai
- **Models:** 46
- **Working tests:** 1 / 46
- **Avg response time:** 2.63s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `claude2` | text | ✅ `ok` | 2.63s | contains expected token 'PONG' |
| `auto` | text | ❌ `invalid` | 7.66s | expected 'PONG', got: 'Sign up and repeat your request.' |
| `claude35haiku` | text | ❌ `empty` | 0.21s | Empty response |
| `claude37sonnetthinking` | text | ❌ `invalid` | 8.01s | expected 'PONG', got: 'Sign up and repeat your request.' |
| `claude3opus` | text | ❌ `empty` | 0.20s | Empty response |
| `claude40opus` | text | ❌ `invalid` | 7.85s | expected 'PONG', got: 'Sign up and repeat your request.' |
| `claude40opus_research` | text | ❌ `invalid` | 7.67s | expected 'PONG', got: 'Sign up and repeat your request.' |
| `claude40opusthinking` | text | ❌ `invalid` | 7.83s | expected 'PONG', got: 'Sign up and repeat your request.' |
| `claude40opusthinking_labs` | text | ❌ `invalid` | 9.33s | expected 'PONG', got: 'Sign up and repeat your request.' |
| `claude40opusthinking_research` | text | ❌ `invalid` | 7.62s | expected 'PONG', got: 'Sign up and repeat your request.' |
| `claude40sonnet_research` | text | ❌ `invalid` | 7.68s | expected 'PONG', got: 'Sign up and repeat your request.' |
| `claude40sonnetthinking_labs` | text | ❌ `invalid` | 7.95s | expected 'PONG', got: 'Sign up and repeat your request.' |
| `claude40sonnetthinking_research` | text | ❌ `invalid` | 7.99s | expected 'PONG', got: 'Sign up and repeat your request.' |
| `claude41opusthinking` | text | ❌ `invalid` | 7.74s | expected 'PONG', got: 'Sign up and repeat your request.' |
| `claude45sonnet` | text | ❌ `invalid` | 7.71s | expected 'PONG', got: 'Sign up and repeat your request.' |
| `claude45sonnetthinking` | text | ❌ `invalid` | 7.68s | expected 'PONG', got: 'Sign up and repeat your request.' |
| `comet_max_assistant` | text | ❌ `invalid` | 7.63s | expected 'PONG', got: 'Sign up and repeat your request.' |
| `experimental` | text | ❌ `invalid` | 7.72s | expected 'PONG', got: 'Sign up and repeat your request.' |
| `gemini` | text | ❌ `rate_limited` | 0.42s | RateLimitError: Response 429: {'status': 'failed', 'error_code': 'RATE_LIMITED', '_response_type': 'RATE_LIMITED', 'text': 'Query rate limit exceeded. Please tr |
| `gemini2flash` | text | ❌ `invalid` | 7.64s | expected 'PONG', got: 'Sign up and repeat your request.' |
| `gpt4` | text | ❌ `invalid` | 7.87s | expected 'PONG', got: 'Sign up and repeat your request.' |
| `gpt41` | text | ❌ `invalid` | 8.22s | expected 'PONG', got: 'Sign up and repeat your request.' |
| `gpt45` | text | ❌ `invalid` | 7.76s | expected 'PONG', got: 'Sign up and repeat your request.' |
| `gpt4o` | text | ❌ `invalid` | 7.97s | expected 'PONG', got: 'Sign up and repeat your request.' |
| `gpt5` | text | ❌ `invalid` | 7.73s | expected 'PONG', got: 'Sign up and repeat your request.' |
| `gpt5_thinking` | text | ❌ `invalid` | 7.83s | expected 'PONG', got: 'Sign up and repeat your request.' |
| `grok` | text | ❌ `invalid` | 7.67s | expected 'PONG', got: 'Sign up and repeat your request.' |
| `grok4` | text | ❌ `invalid` | 7.96s | expected 'PONG', got: 'Sign up and repeat your request.' |
| `llama_x_large` | text | ❌ `empty` | 0.22s | Empty response |
| `mistral` | text | ❌ `empty` | 0.22s | Empty response |
| `o1` | text | ❌ `empty` | 0.21s | Empty response |
| `o3` | text | ❌ `invalid` | 7.70s | expected 'PONG', got: 'Sign up and repeat your request.' |
| `o3_labs` | text | ❌ `invalid` | 7.80s | expected 'PONG', got: 'Sign up and repeat your request.' |
| `o3_research` | text | ❌ `invalid` | 7.99s | expected 'PONG', got: 'Sign up and repeat your request.' |
| `o3mini` | text | ❌ `invalid` | 8.05s | expected 'PONG', got: 'Sign up and repeat your request.' |
| `o3pro` | text | ❌ `invalid` | 7.86s | expected 'PONG', got: 'Sign up and repeat your request.' |
| `o3pro_labs` | text | ❌ `invalid` | 7.69s | expected 'PONG', got: 'Sign up and repeat your request.' |
| `o3pro_research` | text | ❌ `invalid` | 7.62s | expected 'PONG', got: 'Sign up and repeat your request.' |
| `o4mini` | text | ❌ `invalid` | 7.82s | expected 'PONG', got: 'Sign up and repeat your request.' |
| `pplx_alpha` | text | ❌ `invalid` | 7.64s | expected 'PONG', got: 'Sign up and repeat your request.' |
| `pplx_beta` | text | ❌ `invalid` | 7.71s | expected 'PONG', got: 'Sign up and repeat your request.' |
| `pplx_pro` | text | ❌ `invalid` | 7.79s | expected 'PONG', got: 'Sign up and repeat your request.' |
| `pplx_pro_upgraded` | text | ❌ `invalid` | 7.68s | expected 'PONG', got: 'Sign up and repeat your request.' |
| `pplx_reasoning` | text | ❌ `invalid` | 7.77s | expected 'PONG', got: 'Sign up and repeat your request.' |
| `r1` | text | ❌ `invalid` | 8.33s | expected 'PONG', got: 'Sign up and repeat your request.' |
| `turbo` | text | ❌ `invalid` | 7.98s | expected 'PONG', got: 'Sign up and repeat your request.' |

## Sample successful responses

### `claude2` — text

```
PONG
```

