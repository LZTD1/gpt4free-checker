# g4f providers — daily test report

_Generated: `2026-06-09T11:37:19.527898+00:00`_

## Overview

- **Providers:** 6 / 47 working
- **Models discovered:** 149
- **Tests run:** 149
- **Successful:** 12 (8.05%)
- **Avg response time (OK):** 8.036s

## Results by capability

| Capability | Working |
| --- | ---: |
| text | 10 |
| image | 2 |
| audio | 0 |
| video | 0 |

## Results by status

| Status | Count |
| --- | ---: |
| `timeout` | 47 |
| `invalid` | 40 |
| `exception` | 33 |
| `ok` | 12 |
| `empty` | 7 |
| `api_error` | 5 |
| `http_error` | 4 |
| `rate_limited` | 1 |

## Providers

| Provider | Models | OK | Fail | Avg time | Capabilities | Status |
| --- | ---: | ---: | ---: | ---: | --- | :---: |
| [ BlackForestLabs_Flux1Dev ](providers/BlackForestLabs_Flux1Dev.md) | 2 | 1 | 1 | 27.33s | image | ✅ |
| [ CohereForAI_C4AI_Command ](providers/CohereForAI_C4AI_Command.md) | 7 | 4 | 3 | 1.08s | text | ✅ |
| [ OperaAria ](providers/OperaAria.md) | 2 | 2 | 0 | 16.20s | image, text | ✅ |
| [ Perplexity ](providers/Perplexity.md) | 46 | 1 | 45 | 2.63s | text | ✅ |
| [ Qwen ](providers/Qwen.md) | 19 | 3 | 16 | 9.08s | text | ✅ |
| [ Yqcloud ](providers/Yqcloud.md) | 1 | 1 | 0 | 2.53s | text | ✅ |
| [ ApiAirforce ](providers/ApiAirforce.md) | 0 | 0 | 0 | — | — | ❌ |
| [ Azure ](providers/Azure.md) | 0 | 0 | 0 | — | — | ❌ |
| [ BlackForestLabs_Flux1KontextDev ](providers/BlackForestLabs_Flux1KontextDev.md) | 0 | 0 | 0 | — | — | ❌ |
| [ CachedSearch ](providers/CachedSearch.md) | 0 | 0 | 0 | — | — | ❌ |
| [ Chatai ](providers/Chatai.md) | 1 | 0 | 1 | — | — | ❌ |
| [ Claude ](providers/Claude.md) | 0 | 0 | 0 | — | — | ❌ |
| [ Copilot ](providers/Copilot.md) | 4 | 0 | 4 | — | — | ❌ |
| [ CopilotSession ](providers/CopilotSession.md) | 4 | 0 | 4 | — | — | ❌ |
| [ Custom ](providers/Custom.md) | 0 | 0 | 0 | — | — | ❌ |
| [ DeepInfra ](providers/DeepInfra.md) | 0 | 0 | 0 | — | — | ❌ |
| [ DeepseekAI_JanusPro7b ](providers/DeepseekAI_JanusPro7b.md) | 2 | 0 | 2 | — | — | ❌ |
| [ GeminiPro ](providers/GeminiPro.md) | 0 | 0 | 0 | — | — | ❌ |
| [ GoogleSearch ](providers/GoogleSearch.md) | 0 | 0 | 0 | — | — | ❌ |
| [ GradientNetwork ](providers/GradientNetwork.md) | 2 | 0 | 2 | — | — | ❌ |
| [ Groq ](providers/Groq.md) | 0 | 0 | 0 | — | — | ❌ |
| [ HuggingFace ](providers/HuggingFace.md) | 0 | 0 | 0 | — | — | ❌ |
| [ HuggingSpace ](providers/HuggingSpace.md) | 0 | 0 | 0 | — | — | ❌ |
| [ ItalyGPT ](providers/ItalyGPT.md) | 1 | 0 | 1 | — | — | ❌ |
| [ LMArena ](providers/LMArena.md) | 0 | 0 | 0 | — | — | ❌ |
| [ MarkItDown ](providers/MarkItDown.md) | 0 | 0 | 0 | — | — | ❌ |
| [ MetaAI ](providers/MetaAI.md) | 0 | 0 | 0 | — | — | ❌ |
| [ Microsoft_Phi_4_Multimodal ](providers/Microsoft_Phi_4_Multimodal.md) | 1 | 0 | 1 | — | — | ❌ |
| [ Nvidia ](providers/Nvidia.md) | 0 | 0 | 0 | — | — | ❌ |
| [ Ollama ](providers/Ollama.md) | 0 | 0 | 0 | — | — | ❌ |
| [ OllamaSwarm ](providers/OllamaSwarm.md) | 0 | 0 | 0 | — | — | ❌ |
| [ OpenaiChat ](providers/OpenaiChat.md) | 23 | 0 | 23 | — | — | ❌ |
| [ OpenAIFM ](providers/OpenAIFM.md) | 17 | 0 | 17 | — | — | ❌ |
| [ OpenRouterFree ](providers/OpenRouterFree.md) | 0 | 0 | 0 | — | — | ❌ |
| [ Pi ](providers/Pi.md) | 1 | 0 | 1 | — | — | ❌ |
| [ PollinationsAI ](providers/PollinationsAI.md) | 0 | 0 | 0 | — | — | ❌ |
| [ PollinationsAudio ](providers/PollinationsAudio.md) | 0 | 0 | 0 | — | — | ❌ |
| [ PollinationsImage ](providers/PollinationsImage.md) | 0 | 0 | 0 | — | — | ❌ |
| [ Qwen_Qwen_2_5 ](providers/Qwen_Qwen_2_5.md) | 1 | 0 | 1 | — | — | ❌ |
| [ Qwen_Qwen_2_5_Max ](providers/Qwen_Qwen_2_5_Max.md) | 1 | 0 | 1 | — | — | ❌ |
| [ Qwen_Qwen_2_5M ](providers/Qwen_Qwen_2_5M.md) | 1 | 0 | 1 | — | — | ❌ |
| [ Qwen_Qwen_2_72B ](providers/Qwen_Qwen_2_72B.md) | 1 | 0 | 1 | — | — | ❌ |
| [ Qwen_Qwen_3 ](providers/Qwen_Qwen_3.md) | 8 | 0 | 8 | — | — | ❌ |
| [ StabilityAI_SD35Large ](providers/StabilityAI_SD35Large.md) | 1 | 0 | 1 | — | — | ❌ |
| [ StabilityAI_SD35Large ](providers/StabilityAI_SD35Large.md) | 1 | 0 | 1 | — | — | ❌ |
| [ TeachAnything ](providers/TeachAnything.md) | 1 | 0 | 1 | — | — | ❌ |
| [ WeWordle ](providers/WeWordle.md) | 1 | 0 | 1 | — | — | ❌ |
