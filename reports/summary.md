# g4f providers — daily test report

_Generated: `2026-07-18T09:11:08.664415+00:00`_

## Overview

- **Providers:** 7 / 42 working
- **Models discovered:** 214
- **Tests run:** 214
- **Successful:** 20 (9.35%)
- **Avg response time (OK):** 13.991s

## Results by capability

| Capability | Working |
| --- | ---: |
| text | 20 |
| image | 0 |
| audio | 0 |
| video | 0 |

## Results by status

| Status | Count |
| --- | ---: |
| `exception` | 77 |
| `timeout` | 51 |
| `invalid` | 47 |
| `ok` | 20 |
| `empty` | 8 |
| `http_error` | 7 |
| `api_error` | 3 |
| `rate_limited` | 1 |

## Providers

| Provider | Models | OK | Fail | Avg time | Capabilities | Status |
| --- | ---: | ---: | ---: | ---: | --- | :---: |
| [ CohereForAI_C4AI_Command ](providers/CohereForAI_C4AI_Command.md) | 7 | 4 | 3 | 0.30s | text | ✅ |
| [ CopilotApp ](providers/CopilotApp.md) | 5 | 4 | 1 | 0.88s | text | ✅ |
| [ Felo ](providers/Felo.md) | 5 | 2 | 3 | 21.00s | text | ✅ |
| [ Perplexity ](providers/Perplexity.md) | 46 | 2 | 44 | 20.85s | text | ✅ |
| [ Qwen ](providers/Qwen.md) | 23 | 1 | 22 | 42.17s | text | ✅ |
| [ Surfsense ](providers/Surfsense.md) | 2 | 2 | 0 | 21.35s | text | ✅ |
| [ WeWordle ](providers/WeWordle.md) | 7 | 5 | 2 | 21.31s | text | ✅ |
| [ BlackForestLabs_Flux1Dev ](providers/BlackForestLabs_Flux1Dev.md) | 2 | 0 | 2 | — | — | ❌ |
| [ BlackForestLabs_Flux1KontextDev ](providers/BlackForestLabs_Flux1KontextDev.md) | 0 | 0 | 0 | — | — | ❌ |
| [ CachedSearch ](providers/CachedSearch.md) | 0 | 0 | 0 | — | — | ❌ |
| [ Claude ](providers/Claude.md) | 0 | 0 | 0 | — | — | ❌ |
| [ Cloudflare ](providers/Cloudflare.md) | 54 | 0 | 54 | — | — | ❌ |
| [ Copilot ](providers/Copilot.md) | 4 | 0 | 4 | — | — | ❌ |
| [ CopilotSession ](providers/CopilotSession.md) | 4 | 0 | 4 | — | — | ❌ |
| [ Custom ](providers/Custom.md) | 0 | 0 | 0 | — | — | ❌ |
| [ DeepInfra ](providers/DeepInfra.md) | 0 | 0 | 0 | — | — | ❌ |
| [ EasyChat ](providers/EasyChat.md) | 0 | 0 | 0 | — | — | ❌ |
| [ GeminiPro ](providers/GeminiPro.md) | 0 | 0 | 0 | — | — | ❌ |
| [ GLM ](providers/GLM.md) | 0 | 0 | 0 | — | — | ❌ |
| [ GoogleSearch ](providers/GoogleSearch.md) | 0 | 0 | 0 | — | — | ❌ |
| [ Groq ](providers/Groq.md) | 0 | 0 | 0 | — | — | ❌ |
| [ HuggingFace ](providers/HuggingFace.md) | 0 | 0 | 0 | — | — | ❌ |
| [ HuggingSpace ](providers/HuggingSpace.md) | 0 | 0 | 0 | — | — | ❌ |
| [ LMArena ](providers/LMArena.md) | 0 | 0 | 0 | — | — | ❌ |
| [ MarkItDown ](providers/MarkItDown.md) | 0 | 0 | 0 | — | — | ❌ |
| [ MetaAI ](providers/MetaAI.md) | 0 | 0 | 0 | — | — | ❌ |
| [ Miklium ](providers/Miklium.md) | 5 | 0 | 5 | — | — | ❌ |
| [ Nvidia ](providers/Nvidia.md) | 0 | 0 | 0 | — | — | ❌ |
| [ Ollama ](providers/Ollama.md) | 0 | 0 | 0 | — | — | ❌ |
| [ OllamaSwarm ](providers/OllamaSwarm.md) | 0 | 0 | 0 | — | — | ❌ |
| [ OpenaiChat ](providers/OpenaiChat.md) | 23 | 0 | 23 | — | — | ❌ |
| [ OpenAIFM ](providers/OpenAIFM.md) | 17 | 0 | 17 | — | — | ❌ |
| [ OperaAria ](providers/OperaAria.md) | 2 | 0 | 2 | — | — | ❌ |
| [ Perchance ](providers/Perchance.md) | 2 | 0 | 2 | — | — | ❌ |
| [ PhindAi ](providers/PhindAi.md) | 2 | 0 | 2 | — | — | ❌ |
| [ Pi ](providers/Pi.md) | 1 | 0 | 1 | — | — | ❌ |
| [ Pollinations ](providers/Pollinations.md) | 0 | 0 | 0 | — | — | ❌ |
| [ PollinationsAudio ](providers/PollinationsAudio.md) | 0 | 0 | 0 | — | — | ❌ |
| [ PollinationsImage ](providers/PollinationsImage.md) | 0 | 0 | 0 | — | — | ❌ |
| [ StabilityAI_SD35Large ](providers/StabilityAI_SD35Large.md) | 1 | 0 | 1 | — | — | ❌ |
| [ TeachAnything ](providers/TeachAnything.md) | 1 | 0 | 1 | — | — | ❌ |
| [ Yqcloud ](providers/Yqcloud.md) | 1 | 0 | 1 | — | — | ❌ |
