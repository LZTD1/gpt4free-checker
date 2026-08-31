# g4f providers — daily test report

_Generated: `2026-08-31T14:06:51.394999+00:00`_

## Overview

- **Providers:** 5 / 36 working
- **Models discovered:** 204
- **Tests run:** 204
- **Successful:** 21 (10.29%)
- **Avg response time (OK):** 18.256s

## Results by capability

| Capability | Working |
| --- | ---: |
| text | 19 |
| image | 2 |
| audio | 0 |
| video | 0 |

## Results by status

| Status | Count |
| --- | ---: |
| `exception` | 84 |
| `timeout` | 43 |
| `invalid` | 41 |
| `ok` | 21 |
| `empty` | 8 |
| `api_error` | 5 |
| `rate_limited` | 2 |

## Providers

| Provider | Models | OK | Fail | Avg time | Capabilities | Status |
| --- | ---: | ---: | ---: | ---: | --- | :---: |
| [ BlackForestLabs_Flux1Dev ](providers/BlackForestLabs_Flux1Dev.md) | 2 | 2 | 0 | 21.60s | image | ✅ |
| [ CohereForAI_C4AI_Command ](providers/CohereForAI_C4AI_Command.md) | 7 | 3 | 4 | 0.27s | text | ✅ |
| [ Gemini ](providers/Gemini.md) | 17 | 14 | 3 | 19.71s | text | ✅ |
| [ Perplexity ](providers/Perplexity.md) | 46 | 1 | 45 | 20.37s | text | ✅ |
| [ Yqcloud ](providers/Yqcloud.md) | 1 | 1 | 0 | 43.04s | text | ✅ |
| [ BlackForestLabs_Flux1KontextDev ](providers/BlackForestLabs_Flux1KontextDev.md) | 0 | 0 | 0 | — | — | ❌ |
| [ CachedSearch ](providers/CachedSearch.md) | 0 | 0 | 0 | — | — | ❌ |
| [ Claude ](providers/Claude.md) | 0 | 0 | 0 | — | — | ❌ |
| [ Cloudflare ](providers/Cloudflare.md) | 54 | 0 | 54 | — | — | ❌ |
| [ Copilot ](providers/Copilot.md) | 4 | 0 | 4 | — | — | ❌ |
| [ CopilotApp ](providers/CopilotApp.md) | 5 | 0 | 5 | — | — | ❌ |
| [ CopilotSession ](providers/CopilotSession.md) | 4 | 0 | 4 | — | — | ❌ |
| [ Custom ](providers/Custom.md) | 0 | 0 | 0 | — | — | ❌ |
| [ DeepInfra ](providers/DeepInfra.md) | 0 | 0 | 0 | — | — | ❌ |
| [ GeminiPro ](providers/GeminiPro.md) | 0 | 0 | 0 | — | — | ❌ |
| [ GLM ](providers/GLM.md) | 0 | 0 | 0 | — | — | ❌ |
| [ GoogleSearch ](providers/GoogleSearch.md) | 0 | 0 | 0 | — | — | ❌ |
| [ Groq ](providers/Groq.md) | 0 | 0 | 0 | — | — | ❌ |
| [ HuggingFace ](providers/HuggingFace.md) | 0 | 0 | 0 | — | — | ❌ |
| [ HuggingSpace ](providers/HuggingSpace.md) | 0 | 0 | 0 | — | — | ❌ |
| [ LMArena ](providers/LMArena.md) | 0 | 0 | 0 | — | — | ❌ |
| [ MarkItDown ](providers/MarkItDown.md) | 0 | 0 | 0 | — | — | ❌ |
| [ MetaAI ](providers/MetaAI.md) | 0 | 0 | 0 | — | — | ❌ |
| [ Nvidia ](providers/Nvidia.md) | 0 | 0 | 0 | — | — | ❌ |
| [ Ollama ](providers/Ollama.md) | 0 | 0 | 0 | — | — | ❌ |
| [ OpenaiChat ](providers/OpenaiChat.md) | 17 | 0 | 17 | — | — | ❌ |
| [ OpenAIFM ](providers/OpenAIFM.md) | 17 | 0 | 17 | — | — | ❌ |
| [ OperaAria ](providers/OperaAria.md) | 2 | 0 | 2 | — | — | ❌ |
| [ PhindAi ](providers/PhindAi.md) | 2 | 0 | 2 | — | — | ❌ |
| [ Pi ](providers/Pi.md) | 1 | 0 | 1 | — | — | ❌ |
| [ Pollinations ](providers/Pollinations.md) | 0 | 0 | 0 | — | — | ❌ |
| [ PollinationsAudio ](providers/PollinationsAudio.md) | 0 | 0 | 0 | — | — | ❌ |
| [ PollinationsImage ](providers/PollinationsImage.md) | 0 | 0 | 0 | — | — | ❌ |
| [ Qwen ](providers/Qwen.md) | 23 | 0 | 23 | — | — | ❌ |
| [ StabilityAI_SD35Large ](providers/StabilityAI_SD35Large.md) | 1 | 0 | 1 | — | — | ❌ |
| [ TeachAnything ](providers/TeachAnything.md) | 1 | 0 | 1 | — | — | ❌ |
