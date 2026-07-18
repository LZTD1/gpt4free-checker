# Perplexity

- **Label:** Perplexity
- **URL:** https://www.perplexity.ai
- **Models:** 46
- **Working tests:** 2 / 46
- **Avg response time:** 20.85s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `gpt5` | text | ✅ `ok` | 20.67s | contains expected token 'PONG' |
| `o3` | text | ✅ `ok` | 21.03s | contains expected token 'PONG' |
| `auto` | text | ❌ `exception` | 21.61s | AttributeError: 'JsonConversation' object has no attribute 'thread_title' |
| `claude2` | text | ❌ `invalid` | 22.03s | expected 'PONG', got: 'est.' |
| `claude35haiku` | text | ❌ `empty` | 0.07s | Empty response |
| `claude37sonnetthinking` | text | ❌ `invalid` | 20.28s | expected 'PONG', got: 'est.' |
| `claude3opus` | text | ❌ `empty` | 0.12s | Empty response |
| `claude40opus` | text | ❌ `invalid` | 22.03s | expected 'PONG', got: 'est.' |
| `claude40opus_research` | text | ❌ `invalid` | 20.47s | expected 'PONG', got: 'est.' |
| `claude40opusthinking` | text | ❌ `invalid` | 20.47s | expected 'PONG', got: 'est.' |
| `claude40opusthinking_labs` | text | ❌ `invalid` | 7.67s | expected 'PONG', got: 'est.' |
| `claude40opusthinking_research` | text | ❌ `invalid` | 22.03s | expected 'PONG', got: 'est.' |
| `claude40sonnet_research` | text | ❌ `invalid` | 20.38s | expected 'PONG', got: 'est.' |
| `claude40sonnetthinking_labs` | text | ❌ `invalid` | 22.03s | expected 'PONG', got: 'est.' |
| `claude40sonnetthinking_research` | text | ❌ `invalid` | 22.03s | expected 'PONG', got: 'est.' |
| `claude41opusthinking` | text | ❌ `invalid` | 22.03s | expected 'PONG', got: 'est.' |
| `claude45sonnet` | text | ❌ `invalid` | 20.16s | expected 'PONG', got: 'est.' |
| `claude45sonnetthinking` | text | ❌ `invalid` | 22.03s | expected 'PONG', got: 'est.' |
| `comet_max_assistant` | text | ❌ `invalid` | 22.03s | expected 'PONG', got: 'est.' |
| `experimental` | text | ❌ `invalid` | 20.33s | expected 'PONG', got: 'est.' |
| `gemini` | text | ❌ `empty` | 0.08s | Empty response |
| `gemini2flash` | text | ❌ `invalid` | 21.03s | expected 'PONG', got: 'est.' |
| `gpt4` | text | ❌ `invalid` | 7.58s | expected 'PONG', got: 'est.' |
| `gpt41` | text | ❌ `invalid` | 21.03s | expected 'PONG', got: 'est.' |
| `gpt45` | text | ❌ `invalid` | 7.58s | expected 'PONG', got: 'est.' |
| `gpt4o` | text | ❌ `invalid` | 7.58s | expected 'PONG', got: 'est.' |
| `gpt5_thinking` | text | ❌ `invalid` | 22.03s | expected 'PONG', got: 'est.' |
| `grok` | text | ❌ `invalid` | 22.03s | expected 'PONG', got: 'est.' |
| `grok4` | text | ❌ `invalid` | 41.09s | expected 'PONG', got: 'est.' |
| `llama_x_large` | text | ❌ `empty` | 0.14s | Empty response |
| `mistral` | text | ❌ `empty` | 0.09s | Empty response |
| `o1` | text | ❌ `empty` | 0.09s | Empty response |
| `o3_labs` | text | ❌ `invalid` | 21.03s | expected 'PONG', got: 'est.' |
| `o3_research` | text | ❌ `invalid` | 21.03s | expected 'PONG', got: 'est.' |
| `o3mini` | text | ❌ `invalid` | 7.50s | expected 'PONG', got: 'est.' |
| `o3pro` | text | ❌ `invalid` | 21.03s | expected 'PONG', got: 'est.' |
| `o3pro_labs` | text | ❌ `invalid` | 21.03s | expected 'PONG', got: 'est.' |
| `o3pro_research` | text | ❌ `invalid` | 22.03s | expected 'PONG', got: 'est.' |
| `o4mini` | text | ❌ `invalid` | 7.61s | expected 'PONG', got: 'est.' |
| `pplx_alpha` | text | ❌ `invalid` | 41.11s | expected 'PONG', got: 'est.' |
| `pplx_beta` | text | ❌ `invalid` | 21.03s | expected 'PONG', got: 'est.' |
| `pplx_pro` | text | ❌ `invalid` | 20.08s | expected 'PONG', got: 'est.' |
| `pplx_pro_upgraded` | text | ❌ `invalid` | 22.03s | expected 'PONG', got: 'est.' |
| `pplx_reasoning` | text | ❌ `invalid` | 7.58s | expected 'PONG', got: 'est.' |
| `r1` | text | ❌ `invalid` | 7.73s | expected 'PONG', got: 'est.' |
| `turbo` | text | ❌ `invalid` | 22.03s | expected 'PONG', got: 'est.' |

## Sample successful responses

### `gpt5` — text

```
PONG
```

### `o3` — text

```
PONG
```

