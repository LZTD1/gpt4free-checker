# Perplexity

- **Label:** Perplexity
- **URL:** https://www.perplexity.ai
- **Models:** 46
- **Working tests:** 2 / 46
- **Avg response time:** 20.46s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `o3pro_labs` | text | ✅ `ok` | 20.62s | contains expected token 'PONG' |
| `pplx_pro_upgraded` | text | ✅ `ok` | 20.30s | contains expected token 'PONG' |
| `auto` | text | ❌ `invalid` | 20.50s | expected 'PONG', got: 'est.' |
| `claude2` | text | ❌ `invalid` | 21.02s | expected 'PONG', got: 'est.' |
| `claude35haiku` | text | ❌ `empty` | 0.21s | Empty response |
| `claude37sonnetthinking` | text | ❌ `invalid` | 22.03s | expected 'PONG', got: 'est.' |
| `claude3opus` | text | ❌ `empty` | 0.21s | Empty response |
| `claude40opus` | text | ❌ `invalid` | 20.38s | expected 'PONG', got: 'est.' |
| `claude40opus_research` | text | ❌ `invalid` | 22.02s | expected 'PONG', got: 'est.' |
| `claude40opusthinking` | text | ❌ `invalid` | 22.02s | expected 'PONG', got: 'est.' |
| `claude40opusthinking_labs` | text | ❌ `invalid` | 41.16s | expected 'PONG', got: 'est.' |
| `claude40opusthinking_research` | text | ❌ `invalid` | 20.19s | expected 'PONG', got: 'est.' |
| `claude40sonnet_research` | text | ❌ `invalid` | 41.12s | expected 'PONG', got: 'est.' |
| `claude40sonnetthinking_labs` | text | ❌ `invalid` | 22.02s | expected 'PONG', got: 'est.' |
| `claude40sonnetthinking_research` | text | ❌ `invalid` | 20.35s | expected 'PONG', got: 'est.' |
| `claude41opusthinking` | text | ❌ `invalid` | 21.02s | expected 'PONG', got: 'est.' |
| `claude45sonnet` | text | ❌ `invalid` | 20.39s | expected 'PONG', got: 'est.' |
| `claude45sonnetthinking` | text | ❌ `invalid` | 22.03s | expected 'PONG', got: 'est.' |
| `comet_max_assistant` | text | ❌ `invalid` | 21.03s | expected 'PONG', got: 'est.' |
| `experimental` | text | ❌ `invalid` | 21.02s | expected 'PONG', got: 'est.' |
| `gemini` | text | ❌ `rate_limited` | 0.22s | RateLimitError: Response 429: {'status': 'failed', 'error_code': 'RATE_LIMITED', '_response_type': 'RATE_LIMITED', 'text': 'Query rate limit exceeded. Please tr |
| `gemini2flash` | text | ❌ `invalid` | 20.24s | expected 'PONG', got: 'est.' |
| `gpt4` | text | ❌ `invalid` | 7.67s | expected 'PONG', got: 'est.' |
| `gpt41` | text | ❌ `invalid` | 21.03s | expected 'PONG', got: 'est.' |
| `gpt45` | text | ❌ `invalid` | 7.68s | expected 'PONG', got: 'est.' |
| `gpt4o` | text | ❌ `invalid` | 7.76s | expected 'PONG', got: 'est.' |
| `gpt5` | text | ❌ `invalid` | 21.03s | expected 'PONG', got: 'est.' |
| `gpt5_thinking` | text | ❌ `invalid` | 21.03s | expected 'PONG', got: 'est.' |
| `grok` | text | ❌ `invalid` | 21.02s | expected 'PONG', got: 'est.' |
| `grok4` | text | ❌ `invalid` | 22.02s | expected 'PONG', got: 'est.' |
| `llama_x_large` | text | ❌ `empty` | 0.23s | Empty response |
| `mistral` | text | ❌ `empty` | 0.22s | Empty response |
| `o1` | text | ❌ `empty` | 0.21s | Empty response |
| `o3` | text | ❌ `invalid` | 22.03s | expected 'PONG', got: 'est.' |
| `o3_labs` | text | ❌ `invalid` | 22.03s | expected 'PONG', got: 'est.' |
| `o3_research` | text | ❌ `invalid` | 7.61s | expected 'PONG', got: 'est.' |
| `o3mini` | text | ❌ `invalid` | 7.71s | expected 'PONG', got: 'est.' |
| `o3pro` | text | ❌ `invalid` | 21.02s | expected 'PONG', got: 'est.' |
| `o3pro_research` | text | ❌ `invalid` | 22.02s | expected 'PONG', got: 'est.' |
| `o4mini` | text | ❌ `invalid` | 22.03s | expected 'PONG', got: 'est.' |
| `pplx_alpha` | text | ❌ `invalid` | 22.02s | expected 'PONG', got: 'est.' |
| `pplx_beta` | text | ❌ `invalid` | 21.02s | expected 'PONG', got: 'est.' |
| `pplx_pro` | text | ❌ `invalid` | 22.03s | expected 'PONG', got: 'est.' |
| `pplx_reasoning` | text | ❌ `invalid` | 7.56s | expected 'PONG', got: 'est.' |
| `r1` | text | ❌ `invalid` | 7.69s | expected 'PONG', got: 'est.' |
| `turbo` | text | ❌ `invalid` | 22.03s | expected 'PONG', got: 'est.' |

## Sample successful responses

### `pplx_pro_upgraded` — text

```
PONG
```

### `o3pro_labs` — text

```
PONG
```

