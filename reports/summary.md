# g4f providers — daily test report

_Generated: `2026-06-10T10:57:04.565123+00:00`_

## Overview

- **Providers:** 6 / 47 working
- **Models discovered:** 149
- **Tests run:** 149
- **Successful:** 13 (8.72%)
- **Avg response time (OK):** 11.934s

## Results by capability

| Capability | Working |
| --- | ---: |
| text | 9 |
| image | 4 |
| audio | 0 |
| video | 0 |

## Results by status

| Status | Count |
| --- | ---: |
| `timeout` | 43 |
| `invalid` | 41 |
| `exception` | 37 |
| `ok` | 13 |
| `empty` | 8 |
| `http_error` | 4 |
| `api_error` | 3 |

## Providers

| Provider | Models | OK | Fail | Avg time | Capabilities | Status |
| --- | ---: | ---: | ---: | ---: | --- | :---: |
| [ BlackForestLabs_Flux1Dev ](providers/BlackForestLabs_Flux1Dev.md) | 2 | 2 | 0 | 19.98s | image | ✅ |
| [ CohereForAI_C4AI_Command ](providers/CohereForAI_C4AI_Command.md) | 7 | 4 | 3 | 8.60s | text | ✅ |
| [ OperaAria ](providers/OperaAria.md) | 2 | 2 | 0 | 8.16s | image, text | ✅ |
| [ Qwen ](providers/Qwen.md) | 19 | 3 | 16 | 8.24s | text | ✅ |
| [ StabilityAI_SD35Large ](providers/StabilityAI_SD35Large.md) | 1 | 1 | 0 | 35.22s | image | ✅ |
| [ Yqcloud ](providers/Yqcloud.md) | 1 | 1 | 0 | 4.55s | text | ✅ |
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
| [ Perplexity ](providers/Perplexity.md) | 46 | 0 | 46 | — | — | ❌ |
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
| [ TeachAnything ](providers/TeachAnything.md) | 1 | 0 | 1 | — | — | ❌ |
| [ WeWordle ](providers/WeWordle.md) | 1 | 0 | 1 | — | — | ❌ |
