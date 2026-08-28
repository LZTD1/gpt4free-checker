# CopilotApp

- **Label:** Copilot App
- **URL:** https://play.google.com/store/apps/details?id=com.microsoft.copilot
- **Models:** 5
- **Working tests:** 0 / 5
- **Avg response time:** —

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `chat` | text | ❌ `http_error` | 0.12s | WSServerHandshakeError: 460, message='Invalid response status', url='wss://copilot.microsoft.com/c/api/chat?api-version=2&clientSessionId=0a20f8f1-ec2b-4404-b58 |
| `reasoning` | text | ❌ `exception` | 0.12s | WSServerHandshakeError: 460, message='Invalid response status', url='wss://copilot.microsoft.com/c/api/chat?api-version=2&clientSessionId=e91becdb-af6d-407f-bcb |
| `search` | text | ❌ `http_error` | 0.14s | WSServerHandshakeError: 460, message='Invalid response status', url='wss://copilot.microsoft.com/c/api/chat?api-version=2&clientSessionId=6caf9016-0767-404e-8e4 |
| `smart` | text | ❌ `exception` | 0.12s | WSServerHandshakeError: 460, message='Invalid response status', url='wss://copilot.microsoft.com/c/api/chat?api-version=2&clientSessionId=9ce0c14f-6319-4a03-936 |
| `study` | text | ❌ `exception` | 0.16s | WSServerHandshakeError: 460, message='Invalid response status', url='wss://copilot.microsoft.com/c/api/chat?api-version=2&clientSessionId=c4327a1b-d6f0-4885-a64 |
