# Gemini

- **Label:** Google Gemini
- **URL:** https://gemini.google.com
- **Models:** 13
- **Working tests:** 4 / 13
- **Avg response time:** 16.45s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `gemini-2.0` | text | ✅ `ok` | 21.03s | contains expected token 'PONG' |
| `gemini-2.0-flash` | text | ✅ `ok` | 2.36s | contains expected token 'PONG' |
| `gemini-2.5-flash` | text | ✅ `ok` | 21.56s | contains expected token 'PONG' |
| `gemini-auto` | text | ✅ `ok` | 20.87s | contains expected token 'PONG' |
| `gemini-2.0-flash-thinking` | text | ❌ `api_error` | 0.00s | MissingAuthError: Gemini session is unauthenticated; model 'gemini-3.5-flash-thinking' would fall back to Flash |
| `gemini-2.0-flash-thinking-with-apps` | text | ❌ `api_error` | 0.00s | MissingAuthError: Gemini session is unauthenticated; model 'gemini-3.5-flash-thinking' would fall back to Flash |
| `gemini-2.5-pro` | text | ❌ `api_error` | 0.00s | MissingAuthError: Gemini session is unauthenticated; model 'gemini-3.1-pro' would fall back to Flash |
| `gemini-3.1-flash-lite` | text | ❌ `api_error` | 0.00s | MissingAuthError: Gemini session is unauthenticated; model 'gemini-flash-lite' would fall back to Flash |
| `gemini-3.1-pro` | text | ❌ `api_error` | 0.00s | MissingAuthError: Gemini session is unauthenticated; model 'gemini-3.1-pro' would fall back to Flash |
| `gemini-3.5-flash` | image | ❌ `exception` | 0.97s | NoMediaResponseError: No media response from Gemini |
| `gemini-3.5-flash-thinking` | text | ❌ `api_error` | 0.00s | MissingAuthError: Gemini session is unauthenticated; model 'gemini-3.5-flash-thinking' would fall back to Flash |
| `gemini-3.5-flash-thinking-lite` | text | ❌ `api_error` | 0.00s | MissingAuthError: Gemini session is unauthenticated; model 'gemini-3.5-flash-thinking-lite' would fall back to Flash |
| `gemini-flash-lite` | text | ❌ `api_error` | 0.00s | MissingAuthError: Gemini session is unauthenticated; model 'gemini-flash-lite' would fall back to Flash |

## Sample successful responses

### `gemini-auto` — text

```
PONG
```

### `gemini-2.0` — text

```
PONG
```

### `gemini-2.0-flash` — text

```
PONG
```

### `gemini-2.5-flash` — text

```
PONG
```

