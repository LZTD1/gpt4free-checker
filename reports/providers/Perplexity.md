# Perplexity

- **Label:** Perplexity
- **URL:** https://www.perplexity.ai
- **Models:** 46
- **Working tests:** 1 / 46
- **Avg response time:** 1.55s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `grok` | text | ✅ `ok` | 1.55s | contains expected token 'PONG' |
| `auto` | text | ❌ `invalid` | 20.20s | expected 'PONG', got: 'est.' |
| `claude2` | text | ❌ `invalid` | 20.39s | expected 'PONG', got: 'est.' |
| `claude35haiku` | text | ❌ `empty` | 0.15s | Empty response |
| `claude37sonnetthinking` | text | ❌ `invalid` | 22.02s | expected 'PONG', got: 'est.' |
| `claude3opus` | text | ❌ `rate_limited` | 0.13s | RateLimitError: Response 429: {'status': 'failed', 'error_code': 'RATE_LIMITED', '_response_type': 'RATE_LIMITED', 'text': 'Query rate limit exceeded. Please tr |
| `claude40opus` | text | ❌ `invalid` | 41.12s | expected 'PONG', got: 'est.' |
| `claude40opus_research` | text | ❌ `invalid` | 21.02s | expected 'PONG', got: 'est.' |
| `claude40opusthinking` | text | ❌ `invalid` | 21.03s | expected 'PONG', got: 'est.' |
| `claude40opusthinking_labs` | text | ❌ `invalid` | 22.03s | expected 'PONG', got: 'est.' |
| `claude40opusthinking_research` | text | ❌ `invalid` | 21.02s | expected 'PONG', got: 'est.' |
| `claude40sonnet_research` | text | ❌ `invalid` | 20.30s | expected 'PONG', got: 'est.' |
| `claude40sonnetthinking_labs` | text | ❌ `invalid` | 21.02s | expected 'PONG', got: 'est.' |
| `claude40sonnetthinking_research` | text | ❌ `invalid` | 22.02s | expected 'PONG', got: 'est.' |
| `claude41opusthinking` | text | ❌ `invalid` | 21.03s | expected 'PONG', got: 'est.' |
| `claude45sonnet` | text | ❌ `invalid` | 20.15s | expected 'PONG', got: 'est.' |
| `claude45sonnetthinking` | text | ❌ `invalid` | 22.02s | expected 'PONG', got: 'est.' |
| `comet_max_assistant` | text | ❌ `invalid` | 22.02s | expected 'PONG', got: 'est.' |
| `experimental` | text | ❌ `invalid` | 20.37s | expected 'PONG', got: 'est.' |
| `gemini` | text | ❌ `rate_limited` | 0.16s | RateLimitError: Response 429: {'status': 'failed', 'error_code': 'RATE_LIMITED', '_response_type': 'RATE_LIMITED', 'text': 'Query rate limit exceeded. Please tr |
| `gemini2flash` | text | ❌ `invalid` | 21.03s | expected 'PONG', got: 'est.' |
| `gpt4` | text | ❌ `invalid` | 3.47s | expected 'PONG', got: 'est.' |
| `gpt41` | text | ❌ `invalid` | 41.11s | expected 'PONG', got: 'est.' |
| `gpt45` | text | ❌ `invalid` | 3.49s | expected 'PONG', got: 'est.' |
| `gpt4o` | text | ❌ `invalid` | 3.53s | expected 'PONG', got: 'est.' |
| `gpt5` | text | ❌ `invalid` | 20.11s | expected 'PONG', got: 'est.' |
| `gpt5_thinking` | text | ❌ `invalid` | 22.03s | expected 'PONG', got: 'est.' |
| `grok4` | text | ❌ `invalid` | 21.02s | expected 'PONG', got: 'est.' |
| `llama_x_large` | text | ❌ `empty` | 0.17s | Empty response |
| `mistral` | text | ❌ `empty` | 0.14s | Empty response |
| `o1` | text | ❌ `empty` | 0.14s | Empty response |
| `o3` | text | ❌ `invalid` | 21.03s | expected 'PONG', got: 'est.' |
| `o3_labs` | text | ❌ `invalid` | 21.02s | expected 'PONG', got: 'est.' |
| `o3_research` | text | ❌ `invalid` | 20.51s | expected 'PONG', got: 'est.' |
| `o3mini` | text | ❌ `invalid` | 3.41s | expected 'PONG', got: 'est.' |
| `o3pro` | text | ❌ `invalid` | 22.03s | expected 'PONG', got: 'est.' |
| `o3pro_labs` | text | ❌ `invalid` | 22.02s | expected 'PONG', got: 'est.' |
| `o3pro_research` | text | ❌ `invalid` | 22.02s | expected 'PONG', got: 'est.' |
| `o4mini` | text | ❌ `invalid` | 3.55s | expected 'PONG', got: 'est.' |
| `pplx_alpha` | text | ❌ `invalid` | 22.02s | expected 'PONG', got: 'est.' |
| `pplx_beta` | text | ❌ `invalid` | 20.48s | expected 'PONG', got: 'est.' |
| `pplx_pro` | text | ❌ `invalid` | 22.02s | expected 'PONG', got: 'est.' |
| `pplx_pro_upgraded` | text | ❌ `invalid` | 20.12s | expected 'PONG', got: 'est.' |
| `pplx_reasoning` | text | ❌ `rate_limited` | 0.19s | RateLimitError: Response 429: {'status': 'failed', 'error_code': 'RATE_LIMITED', '_response_type': 'RATE_LIMITED', 'text': 'Query rate limit exceeded. Please tr |
| `r1` | text | ❌ `invalid` | 3.59s | expected 'PONG', got: 'est.' |
| `turbo` | text | ❌ `invalid` | 22.03s | expected 'PONG', got: 'est.' |

## Sample successful responses

### `grok` — text

```
PONG
```

