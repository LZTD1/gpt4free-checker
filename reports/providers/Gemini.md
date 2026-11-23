# Gemini

- **Label:** Google Gemini
- **URL:** https://gemini.google.com
- **Models:** 17
- **Working tests:** 11 / 17
- **Avg response time:** 21.50s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `gemini-2.0` | text | ✅ `ok` | 21.03s | contains expected token 'PONG' |
| `gemini-2.0-flash-thinking` | text | ✅ `ok` | 22.18s | contains expected token 'PONG' |
| `gemini-2.0-flash-thinking-with-apps` | text | ✅ `ok` | 21.02s | contains expected token 'PONG' |
| `gemini-2.5-flash` | text | ✅ `ok` | 21.02s | contains expected token 'PONG' |
| `gemini-3.1-flash-lite` | text | ✅ `ok` | 22.02s | contains expected token 'PONG' |
| `gemini-3.5-flash` | text | ✅ `ok` | 20.41s | contains expected token 'PONG' |
| `gemini-3.5-flash-lite` | text | ✅ `ok` | 21.83s | contains expected token 'PONG' |
| `gemini-3.5-flash-thinking` | text | ✅ `ok` | 22.31s | contains expected token 'PONG' |
| `gemini-3.5-flash-thinking-lite` | text | ✅ `ok` | 20.20s | contains expected token 'PONG' |
| `gemini-3.6-flash-thinking` | text | ✅ `ok` | 23.44s | contains expected token 'PONG' |
| `gemini-flash-lite` | text | ✅ `ok` | 21.03s | contains expected token 'PONG' |
| `gemini-2.0-flash` | text | ❌ `timeout` | 45.00s | Timeout limit exceeded |
| `gemini-2.5-pro` | text | ❌ `api_error` | 0.00s | MissingAuthError: Gemini session is unauthenticated; model 'gemini-3.1-pro' would fall back to Flash |
| `gemini-3.1-pro` | text | ❌ `api_error` | 0.00s | MissingAuthError: Gemini session is unauthenticated; model 'gemini-3.1-pro' would fall back to Flash |
| `gemini-3.5-flash-lite-thinking` | text | ❌ `timeout` | 45.00s | Timeout limit exceeded |
| `gemini-3.6-flash` | image | ❌ `exception` | 21.05s | NoMediaResponseError: No media response from Gemini |
| `gemini-auto` | text | ❌ `timeout` | 63.29s | Timeout limit exceeded |

## Sample successful responses

### `gemini-3.5-flash-lite` — text

```
PONG
```

### `gemini-2.0` — text

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

### `gemini-3.5-flash` — text

```
PONG
```

### `gemini-3.5-flash-thinking` — text

```
PONG
```

### `gemini-3.6-flash-thinking` — text

```
PONG
```

### `gemini-3.5-flash-thinking-lite` — text

```
PONG
```

