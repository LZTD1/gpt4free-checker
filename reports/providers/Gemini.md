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
| `gemini-2.0` | text | ❌ `rate_limited` | 43.51s | RateLimitError: Response 429: <!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head><meta http-equiv="content-type" content="text/html; c |
| `gemini-2.0-flash` | text | ❌ `rate_limited` | 43.61s | RateLimitError: Response 429: <!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head><meta http-equiv="content-type" content="text/html; c |
| `gemini-2.0-flash-thinking` | text | ❌ `rate_limited` | 43.35s | RateLimitError: Response 429: <!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head><meta http-equiv="content-type" content="text/html; c |
| `gemini-2.5-flash` | text | ❌ `rate_limited` | 43.42s | RateLimitError: Response 429: <!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head><meta http-equiv="content-type" content="text/html; c |
| `gemini-2.5-pro` | text | ❌ `api_error` | 0.00s | MissingAuthError: Gemini session is unauthenticated; model 'gemini-3.1-pro' would fall back to Flash |
| `gemini-3.1-flash-lite` | text | ❌ `rate_limited` | 43.60s | RateLimitError: Response 429: <!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head><meta http-equiv="content-type" content="text/html; c |
| `gemini-3.1-pro` | text | ❌ `api_error` | 0.00s | MissingAuthError: Gemini session is unauthenticated; model 'gemini-3.1-pro' would fall back to Flash |
| `gemini-3.5-flash` | text | ❌ `rate_limited` | 43.38s | RateLimitError: Response 429: <!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head><meta http-equiv="content-type" content="text/html; c |
| `gemini-3.5-flash-lite` | text | ❌ `rate_limited` | 43.40s | RateLimitError: Response 429: <!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head><meta http-equiv="content-type" content="text/html; c |
| `gemini-3.5-flash-lite-thinking` | text | ❌ `rate_limited` | 43.40s | RateLimitError: Response 429: <!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head><meta http-equiv="content-type" content="text/html; c |
| `gemini-3.5-flash-thinking` | text | ❌ `rate_limited` | 22.62s | RateLimitError: Response 429: <!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head><meta http-equiv="content-type" content="text/html; c |
| `gemini-3.5-flash-thinking-lite` | text | ❌ `rate_limited` | 43.63s | RateLimitError: Response 429: <!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head><meta http-equiv="content-type" content="text/html; c |
| `gemini-3.6-flash` | image | ❌ `rate_limited` | 22.48s | RateLimitError: Response 429: <!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head><meta http-equiv="content-type" content="text/html; c |
| `gemini-3.6-flash-thinking` | text | ❌ `exception` | 0.65s | ResponseStatusError: Response 405: )]}'

102
[["er",null,null,null,null,405,null,null,null,9],["di",36],["af.httprm",36,"7605853299126233260",7]]
25
[["e",4,nul |
| `gemini-auto` | text | ❌ `rate_limited` | 43.50s | RateLimitError: Response 429: <!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head><meta http-equiv="content-type" content="text/html; c |
| `gemini-flash-lite` | text | ❌ `rate_limited` | 43.52s | RateLimitError: Response 429: <!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head><meta http-equiv="content-type" content="text/html; c |

## Sample successful responses

### `gemini-2.0-flash-thinking-with-apps` — text

```
PONG
```

