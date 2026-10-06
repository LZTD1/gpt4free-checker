# CopilotApp

- **Label:** Copilot App
- **URL:** https://play.google.com/store/apps/details?id=com.microsoft.copilot
- **Models:** 5
- **Working tests:** 0 / 5
- **Avg response time:** —

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `chat` | text | ❌ `exception` | 20.12s | RuntimeError: Failed to start conversation: {"type":"https://tools.ietf.org/html/rfc9110#section-15.6.1","title":"An error occurred while processing your reques |
| `reasoning` | text | ❌ `http_error` | 0.15s | WSServerHandshakeError: 460, message='Invalid response status', url='wss://copilot.microsoft.com/c/api/chat?api-version=2&clientSessionId=bbf9b233-f03a-4040-abd |
| `search` | text | ❌ `exception` | 21.13s | WSServerHandshakeError: 460, message='Invalid response status', url='wss://copilot.microsoft.com/c/api/chat?api-version=2&clientSessionId=95d179d9-0b7c-424b-9eb |
| `smart` | text | ❌ `exception` | 0.19s | WSServerHandshakeError: 460, message='Invalid response status', url='wss://copilot.microsoft.com/c/api/chat?api-version=2&clientSessionId=7e987275-8848-4861-856 |
| `study` | text | ❌ `exception` | 22.36s | WSServerHandshakeError: 460, message='Invalid response status', url='wss://copilot.microsoft.com/c/api/chat?api-version=2&clientSessionId=5f48d6f9-04a3-485b-a7c |
