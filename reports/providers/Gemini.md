# Gemini

- **Label:** Google Gemini
- **URL:** https://gemini.google.com
- **Models:** 17
- **Working tests:** 9 / 17
- **Avg response time:** 36.46s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `gemini-2.0` | text | ✅ `ok` | 41.38s | contains expected token 'PONG' |
| `gemini-2.0-flash` | text | ✅ `ok` | 42.09s | contains expected token 'PONG' |
| `gemini-2.0-flash-thinking` | text | ✅ `ok` | 42.35s | contains expected token 'PONG' |
| `gemini-2.0-flash-thinking-with-apps` | text | ✅ `ok` | 27.99s | contains expected token 'PONG' |
| `gemini-2.5-flash` | text | ✅ `ok` | 22.27s | contains expected token 'PONG' |
| `gemini-3.1-flash-lite` | text | ✅ `ok` | 44.39s | contains expected token 'PONG' |
| `gemini-3.5-flash-lite` | text | ✅ `ok` | 21.55s | contains expected token 'PONG' |
| `gemini-3.5-flash-lite-thinking` | text | ✅ `ok` | 43.05s | contains expected token 'PONG' |
| `gemini-auto` | text | ✅ `ok` | 43.05s | contains expected token 'PONG' |
| `gemini-2.5-pro` | text | ❌ `api_error` | 0.00s | MissingAuthError: Gemini session is unauthenticated; model 'gemini-3.1-pro' would fall back to Flash |
| `gemini-3.1-pro` | text | ❌ `api_error` | 0.00s | MissingAuthError: Gemini session is unauthenticated; model 'gemini-3.1-pro' would fall back to Flash |
| `gemini-3.5-flash` | text | ❌ `timeout` | 45.00s | Timeout limit exceeded |
| `gemini-3.5-flash-thinking` | text | ❌ `timeout` | 64.90s | Timeout limit exceeded |
| `gemini-3.5-flash-thinking-lite` | text | ❌ `timeout` | 63.48s | Timeout limit exceeded |
| `gemini-3.6-flash` | image | ❌ `exception` | 21.03s | NoMediaResponseError: No media response from Gemini |
| `gemini-3.6-flash-thinking` | text | ❌ `invalid` | 22.03s | expected 'PONG', got: 'I seem to be encountering an error. Can I try something else for you?' |
| `gemini-flash-lite` | text | ❌ `timeout` | 64.71s | Timeout limit exceeded |

## Sample successful responses

### `gemini-3.5-flash-lite` — text

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

### `gemini-2.0-flash-thinking` — text

```
PONG
```

### `gemini-2.0-flash-thinking-with-apps` — text

```
PONG
```

### `gemini-2.5-flash` — text

```
PONG
```

### `gemini-3.1-flash-lite` — text

```
PONG
```

### `gemini-auto` — text

```
PONG
```

### `gemini-3.5-flash-lite-thinking` — text

```
PONG
```

