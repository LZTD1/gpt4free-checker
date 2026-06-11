# g4f providers — daily test report

_Generated: `2026-06-11T11:32:35.411123+00:00`_

## Overview

- **Providers:** 3 / 45 working
- **Models discovered:** 147
- **Tests run:** 147
- **Successful:** 6 (4.08%)
- **Avg response time (OK):** 3.603s

## Results by capability

| Capability | Working |
| --- | ---: |
| text | 5 |
| image | 1 |
| audio | 0 |
| video | 0 |

## Results by status

| Status | Count |
| --- | ---: |
| `timeout` | 48 |
| `invalid` | 42 |
| `api_error` | 25 |
| `exception` | 15 |
| `empty` | 8 |
| `ok` | 6 |
| `http_error` | 3 |

## Providers

| Provider | Models | OK | Fail | Avg time | Capabilities | Status |
| --- | ---: | ---: | ---: | ---: | --- | :---: |
| [ CohereForAI_C4AI_Command ](providers/CohereForAI_C4AI_Command.md) | 7 | 3 | 4 | 0.21s | text | ✅ |
| [ OperaAria ](providers/OperaAria.md) | 2 | 2 | 0 | 9.38s | image, text | ✅ |
| [ Perplexity ](providers/Perplexity.md) | 46 | 1 | 45 | 2.23s | text | ✅ |
| [ ApiAirforce ](providers/ApiAirforce.md) | 0 | 0 | 0 | — | — | ❌ |
| [ BlackForestLabs_Flux1Dev ](providers/BlackForestLabs_Flux1Dev.md) | 2 | 0 | 2 | — | — | ❌ |
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
| [ Qwen ](providers/Qwen.md) | 19 | 0 | 19 | — | — | ❌ |
| [ Qwen_Qwen_2_5 ](providers/Qwen_Qwen_2_5.md) | 1 | 0 | 1 | — | — | ❌ |
| [ Qwen_Qwen_2_5_Max ](providers/Qwen_Qwen_2_5_Max.md) | 1 | 0 | 1 | — | — | ❌ |
| [ Qwen_Qwen_2_5M ](providers/Qwen_Qwen_2_5M.md) | 1 | 0 | 1 | — | — | ❌ |
| [ Qwen_Qwen_2_72B ](providers/Qwen_Qwen_2_72B.md) | 1 | 0 | 1 | — | — | ❌ |
| [ Qwen_Qwen_3 ](providers/Qwen_Qwen_3.md) | 8 | 0 | 8 | — | — | ❌ |
| [ StabilityAI_SD35Large ](providers/StabilityAI_SD35Large.md) | 1 | 0 | 1 | — | — | ❌ |
| [ StabilityAI_SD35Large ](providers/StabilityAI_SD35Large.md) | 1 | 0 | 1 | — | — | ❌ |
| [ TeachAnything ](providers/TeachAnything.md) | 1 | 0 | 1 | — | — | ❌ |
| [ WeWordle ](providers/WeWordle.md) | 1 | 0 | 1 | — | — | ❌ |
| [ Yqcloud ](providers/Yqcloud.md) | 1 | 0 | 1 | — | — | ❌ |
