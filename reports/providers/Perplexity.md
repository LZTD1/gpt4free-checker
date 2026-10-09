# Perplexity

- **Label:** Perplexity
- **URL:** https://www.perplexity.ai
- **Models:** 46
- **Working tests:** 1 / 46
- **Avg response time:** 20.32s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `o3pro_research` | text | ✅ `ok` | 20.32s | contains expected token 'PONG' |
| `auto` | text | ❌ `invalid` | 21.03s | expected 'PONG', got: 'est.' |
| `claude2` | text | ❌ `invalid` | 21.03s | expected 'PONG', got: 'est.' |
| `claude35haiku` | text | ❌ `empty` | 0.20s | Empty response |
| `claude37sonnetthinking` | text | ❌ `invalid` | 22.02s | expected 'PONG', got: 'est.' |
| `claude3opus` | text | ❌ `empty` | 0.51s | Empty response |
| `claude40opus` | text | ❌ `invalid` | 21.03s | expected 'PONG', got: 'est.' |
| `claude40opus_research` | text | ❌ `invalid` | 22.03s | expected 'PONG', got: 'est.' |
| `claude40opusthinking` | text | ❌ `invalid` | 21.03s | expected 'PONG', got: 'est.' |
| `claude40opusthinking_labs` | text | ❌ `invalid` | 3.49s | expected 'PONG', got: 'est.' |
| `claude40opusthinking_research` | text | ❌ `invalid` | 21.03s | expected 'PONG', got: 'est.' |
| `claude40sonnet_research` | text | ❌ `invalid` | 22.03s | expected 'PONG', got: 'est.' |
| `claude40sonnetthinking_labs` | text | ❌ `invalid` | 3.60s | expected 'PONG', got: 'est.' |
| `claude40sonnetthinking_research` | text | ❌ `invalid` | 21.02s | expected 'PONG', got: 'est.' |
| `claude41opusthinking` | text | ❌ `invalid` | 21.03s | expected 'PONG', got: 'est.' |
| `claude45sonnet` | text | ❌ `invalid` | 22.03s | expected 'PONG', got: 'est.' |
| `claude45sonnetthinking` | text | ❌ `invalid` | 21.03s | expected 'PONG', got: 'est.' |
| `comet_max_assistant` | text | ❌ `invalid` | 21.02s | expected 'PONG', got: 'est.' |
| `experimental` | text | ❌ `invalid` | 22.03s | expected 'PONG', got: 'est.' |
| `gemini` | text | ❌ `rate_limited` | 0.20s | RateLimitError: Response 429: {'status': 'failed', 'error_code': 'RATE_LIMITED', '_response_type': 'RATE_LIMITED', 'text': 'Query rate limit exceeded. Please tr |
| `gemini2flash` | text | ❌ `invalid` | 20.44s | expected 'PONG', got: 'est.' |
| `gpt4` | text | ❌ `invalid` | 3.95s | expected 'PONG', got: 'est.' |
| `gpt41` | text | ❌ `invalid` | 21.02s | expected 'PONG', got: 'est.' |
| `gpt45` | text | ❌ `invalid` | 3.48s | expected 'PONG', got: 'est.' |
| `gpt4o` | text | ❌ `invalid` | 4.54s | expected 'PONG', got: 'est.' |
| `gpt5` | text | ❌ `invalid` | 20.45s | expected 'PONG', got: 'est.' |
| `gpt5_thinking` | text | ❌ `invalid` | 22.03s | expected 'PONG', got: 'est.' |
| `grok` | text | ❌ `invalid` | 21.03s | expected 'PONG', got: 'est.' |
| `grok4` | text | ❌ `invalid` | 21.02s | expected 'PONG', got: 'est.' |
| `llama_x_large` | text | ❌ `empty` | 0.46s | Empty response |
| `mistral` | text | ❌ `empty` | 0.24s | Empty response |
| `o1` | text | ❌ `empty` | 0.24s | Empty response |
| `o3` | text | ❌ `invalid` | 21.03s | expected 'PONG', got: 'est.' |
| `o3_labs` | text | ❌ `invalid` | 20.23s | expected 'PONG', got: 'est.' |
| `o3_research` | text | ❌ `invalid` | 21.02s | expected 'PONG', got: 'est.' |
| `o3mini` | text | ❌ `invalid` | 3.65s | expected 'PONG', got: 'est.' |
| `o3pro` | text | ❌ `invalid` | 21.03s | expected 'PONG', got: 'est.' |
| `o3pro_labs` | text | ❌ `invalid` | 22.03s | expected 'PONG', got: 'est.' |
| `o4mini` | text | ❌ `invalid` | 3.47s | expected 'PONG', got: 'est.' |
| `pplx_alpha` | text | ❌ `invalid` | 22.03s | expected 'PONG', got: 'est.' |
| `pplx_beta` | text | ❌ `invalid` | 21.02s | expected 'PONG', got: 'est.' |
| `pplx_pro` | text | ❌ `invalid` | 22.03s | expected 'PONG', got: 'est.' |
| `pplx_pro_upgraded` | text | ❌ `invalid` | 20.14s | expected 'PONG', got: 'est.' |
| `pplx_reasoning` | text | ❌ `invalid` | 3.50s | expected 'PONG', got: 'est.' |
| `r1` | text | ❌ `invalid` | 3.86s | expected 'PONG', got: 'est.' |
| `turbo` | text | ❌ `invalid` | 22.03s | expected 'PONG', got: 'est.' |

## Sample successful responses

### `o3pro_research` — text

```
PONG
```

