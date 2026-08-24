# Gemini

- **Label:** Google Gemini
- **URL:** https://gemini.google.com
- **Models:** 17
- **Working tests:** 14 / 17
- **Avg response time:** 18.46s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `gemini-2.0` | text | ✅ `ok` | 21.03s | contains expected token 'PONG' |
| `gemini-2.0-flash` | text | ✅ `ok` | 20.39s | contains expected token 'PONG' |
| `gemini-2.0-flash-thinking` | text | ✅ `ok` | 20.65s | contains expected token 'PONG' |
| `gemini-2.0-flash-thinking-with-apps` | text | ✅ `ok` | 22.03s | contains expected token 'PONG' |
| `gemini-2.5-flash` | text | ✅ `ok` | 21.03s | contains expected token 'PONG' |
| `gemini-3.1-flash-lite` | text | ✅ `ok` | 22.03s | contains expected token 'PONG' |
| `gemini-3.5-flash` | text | ✅ `ok` | 20.40s | contains expected token 'PONG' |
| `gemini-3.5-flash-lite` | text | ✅ `ok` | 21.70s | contains expected token 'PONG' |
| `gemini-3.5-flash-lite-thinking` | text | ✅ `ok` | 1.76s | contains expected token 'PONG' |
| `gemini-3.5-flash-thinking` | text | ✅ `ok` | 22.03s | contains expected token 'PONG' |
| `gemini-3.5-flash-thinking-lite` | text | ✅ `ok` | 21.65s | contains expected token 'PONG' |
| `gemini-3.6-flash-thinking` | text | ✅ `ok` | 20.19s | contains expected token 'PONG' |
| `gemini-auto` | text | ✅ `ok` | 1.68s | contains expected token 'PONG' |
| `gemini-flash-lite` | text | ✅ `ok` | 21.86s | contains expected token 'PONG' |
| `gemini-2.5-pro` | text | ❌ `api_error` | 0.00s | MissingAuthError: Gemini session is unauthenticated; model 'gemini-3.1-pro' would fall back to Flash |
| `gemini-3.1-pro` | text | ❌ `api_error` | 0.00s | MissingAuthError: Gemini session is unauthenticated; model 'gemini-3.1-pro' would fall back to Flash |
| `gemini-3.6-flash` | image | ❌ `exception` | 21.03s | NoMediaResponseError: No media response from Gemini |

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

