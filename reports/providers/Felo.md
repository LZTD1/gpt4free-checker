# Felo

- **Label:** Felo
- **URL:** https://felo.ai
- **Models:** 5
- **Working tests:** 3 / 5
- **Avg response time:** 6.56s

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `felo-chat` | text | ✅ `ok` | 1.53s | contains expected token 'PONG' |
| `felo-document` | text | ✅ `ok` | 7.70s | contains expected token 'PONG' |
| `felo-scholar` | text | ✅ `ok` | 10.43s | contains expected token 'PONG' |
| `felo-search` | text | ❌ `exception` | 16.38s | TypeError: sequence item 2: expected str instance, Sources found |
| `felo-social` | text | ❌ `exception` | 6.60s | TypeError: sequence item 2: expected str instance, Sources found |

## Sample successful responses

### `felo-chat` — text

```
PONG
```

### `felo-scholar` — text

```
PONG
```

### `felo-document` — text

```
PONG
```

