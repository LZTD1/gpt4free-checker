# Gemini

- **Label:** Google Gemini
- **URL:** https://gemini.google.com
- **Models:** 17
- **Working tests:** 0 / 17
- **Avg response time:** —

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `gemini-2.0` | text | ❌ `invalid` | 21.03s | expected 'PONG', got: 'I encountered an error doing what you asked. Could you try again?' |
| `gemini-2.0-flash` | text | ❌ `invalid` | 20.18s | expected 'PONG', got: "I'm having a hard time fulfilling your request. Can I help you with something el" |
| `gemini-2.0-flash-thinking` | text | ❌ `invalid` | 22.03s | expected 'PONG', got: "I'm having a hard time fulfilling your request. Can I help you with something el" |
| `gemini-2.0-flash-thinking-with-apps` | text | ❌ `invalid` | 21.03s | expected 'PONG', got: 'I seem to be encountering an error. Can I try something else for you?' |
| `gemini-2.5-flash` | text | ❌ `invalid` | 22.03s | expected 'PONG', got: 'Sorry, something went wrong. Please try your request again.' |
| `gemini-2.5-pro` | text | ❌ `api_error` | 0.00s | MissingAuthError: Gemini session is unauthenticated; model 'gemini-3.1-pro' would fall back to Flash |
| `gemini-3.1-flash-lite` | text | ❌ `invalid` | 22.02s | expected 'PONG', got: 'Sorry, something went wrong. Please try your request again.' |
| `gemini-3.1-pro` | text | ❌ `api_error` | 0.00s | MissingAuthError: Gemini session is unauthenticated; model 'gemini-3.1-pro' would fall back to Flash |
| `gemini-3.5-flash` | text | ❌ `invalid` | 20.42s | expected 'PONG', got: 'I seem to be encountering an error. Can I try something else for you?' |
| `gemini-3.5-flash-lite` | text | ❌ `invalid` | 20.24s | expected 'PONG', got: "I'm having a hard time fulfilling your request. Can I help you with something el" |
| `gemini-3.5-flash-lite-thinking` | text | ❌ `invalid` | 21.03s | expected 'PONG', got: "I'm having a hard time fulfilling your request. Can I help you with something el" |
| `gemini-3.5-flash-thinking` | text | ❌ `invalid` | 22.03s | expected 'PONG', got: "I'm having a hard time fulfilling your request. Can I help you with something el" |
| `gemini-3.5-flash-thinking-lite` | text | ❌ `invalid` | 22.03s | expected 'PONG', got: "I'm having a hard time fulfilling your request. Can I help you with something el" |
| `gemini-3.6-flash` | image | ❌ `exception` | 21.04s | NoMediaResponseError: No media response from Gemini |
| `gemini-3.6-flash-thinking` | text | ❌ `invalid` | 21.03s | expected 'PONG', got: 'I seem to be encountering an error. Can I try something else for you?' |
| `gemini-auto` | text | ❌ `invalid` | 20.45s | expected 'PONG', got: "I'm having a hard time fulfilling your request. Can I help you with something el" |
| `gemini-flash-lite` | text | ❌ `invalid` | 22.03s | expected 'PONG', got: 'Sorry, something went wrong. Please try your request again.' |
