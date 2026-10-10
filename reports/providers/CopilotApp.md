# CopilotApp

- **Label:** Copilot App
- **URL:** https://play.google.com/store/apps/details?id=com.microsoft.copilot
- **Models:** 5
- **Working tests:** 0 / 5
- **Avg response time:** —

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `chat` | text | ❌ `exception` | 0.18s | WSServerHandshakeError: 460, message='Invalid response status', url='wss://copilot.microsoft.com/c/api/chat?api-version=2&clientSessionId=6c6ade8f-dfa1-43eb-b19 |
| `reasoning` | text | ❌ `exception` | 0.20s | WSServerHandshakeError: 460, message='Invalid response status', url='wss://copilot.microsoft.com/c/api/chat?api-version=2&clientSessionId=6c83e5f4-c853-45a8-91e |
| `search` | text | ❌ `http_error` | 0.13s | WSServerHandshakeError: 460, message='Invalid response status', url='wss://copilot.microsoft.com/c/api/chat?api-version=2&clientSessionId=366e6956-009b-41dc-840 |
| `smart` | text | ❌ `exception` | 0.17s | WSServerHandshakeError: 460, message='Invalid response status', url='wss://copilot.microsoft.com/c/api/chat?api-version=2&clientSessionId=502c4fdb-ee22-46af-a51 |
| `study` | text | ❌ `exception` | 0.18s | WSServerHandshakeError: 460, message='Invalid response status', url='wss://copilot.microsoft.com/c/api/chat?api-version=2&clientSessionId=5f9f607f-06d5-4353-bc6 |
