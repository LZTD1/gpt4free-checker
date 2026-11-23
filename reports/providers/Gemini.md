# Gemini

- **Label:** Google Gemini
- **URL:** https://gemini.google.com
- **Models:** 17
- **Working tests:** 1 / 17
- **Avg response time:** 21.03s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `gemini-2.0-flash-thinking-with-apps` | text | ✅ `ok` | 21.03s | contains expected token 'PONG' |
| `gemini-2.0` | text | ❌ `rate_limited` | 22.54s | RateLimitError: Response 429: <!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head><meta http-equiv="content-type" content="text/html; c |
| `gemini-2.0-flash` | text | ❌ `rate_limited` | 43.40s | RateLimitError: Response 429: <!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head><meta http-equiv="content-type" content="text/html; c |
| `gemini-2.0-flash-thinking` | text | ❌ `rate_limited` | 43.62s | RateLimitError: Response 429: <!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head><meta http-equiv="content-type" content="text/html; c |
| `gemini-2.5-flash` | text | ❌ `rate_limited` | 43.60s | RateLimitError: Response 429: <!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head><meta http-equiv="content-type" content="text/html; c |
| `gemini-2.5-pro` | text | ❌ `api_error` | 0.00s | MissingAuthError: Gemini session is unauthenticated; model 'gemini-3.1-pro' would fall back to Flash |
| `gemini-3.1-flash-lite` | text | ❌ `rate_limited` | 43.54s | RateLimitError: Response 429: <!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head><meta http-equiv="content-type" content="text/html; c |
| `gemini-3.1-pro` | text | ❌ `api_error` | 0.00s | MissingAuthError: Gemini session is unauthenticated; model 'gemini-3.1-pro' would fall back to Flash |
| `gemini-3.5-flash` | text | ❌ `rate_limited` | 22.34s | RateLimitError: Response 429: <!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head><meta http-equiv="content-type" content="text/html; c |
| `gemini-3.5-flash-lite` | text | ❌ `rate_limited` | 43.51s | RateLimitError: Response 429: <!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head><meta http-equiv="content-type" content="text/html; c |
| `gemini-3.5-flash-lite-thinking` | text | ❌ `rate_limited` | 43.42s | RateLimitError: Response 429: <!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head><meta http-equiv="content-type" content="text/html; c |
| `gemini-3.5-flash-thinking` | text | ❌ `rate_limited` | 43.41s | RateLimitError: Response 429: <!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head><meta http-equiv="content-type" content="text/html; c |
| `gemini-3.5-flash-thinking-lite` | text | ❌ `rate_limited` | 43.57s | RateLimitError: Response 429: <!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head><meta http-equiv="content-type" content="text/html; c |
| `gemini-3.6-flash` | image | ❌ `rate_limited` | 22.45s | RateLimitError: Response 429: <!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head><meta http-equiv="content-type" content="text/html; c |
| `gemini-3.6-flash-thinking` | text | ❌ `timeout` | 64.96s | Timeout limit exceeded |
| `gemini-auto` | text | ❌ `rate_limited` | 43.41s | RateLimitError: Response 429: <!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head><meta http-equiv="content-type" content="text/html; c |
| `gemini-flash-lite` | text | ❌ `rate_limited` | 43.51s | RateLimitError: Response 429: <!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head><meta http-equiv="content-type" content="text/html; c |

## Sample successful responses

### `gemini-2.0-flash-thinking-with-apps` — text

```
PONG
```

