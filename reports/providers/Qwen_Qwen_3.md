# Qwen_Qwen_3

- **Label:** Qwen Qwen-3
- **URL:** https://qwen-qwen3-demo.hf.space
- **Models:** 8
- **Working tests:** 0 / 8
- **Avg response time:** —

## Per-model results

| Model | Capability | Status | Time | Notes |
| --- | --- | :---: | ---: | --- |
| `qwen-3-0.6b` | text | ❌ `exception` | 3.95s | ResponseStatusError: Response 503: {'detail': 'Queue is full. Max size is 100 and size is 100.'} |
| `qwen-3-1.7b` | text | ❌ `exception` | 4.11s | ResponseStatusError: Response 503: {'detail': 'Queue is full. Max size is 100 and size is 100.'} |
| `qwen-3-14b` | text | ❌ `timeout` | 26.28s | Timeout limit exceeded |
| `qwen-3-235b` | text | ❌ `exception` | 4.72s | ResponseStatusError: Response 503: {'detail': 'Queue is full. Max size is 100 and size is 100.'} |
| `qwen-3-30b-a3b` | text | ❌ `exception` | 4.72s | ResponseStatusError: Response 503: {'detail': 'Queue is full. Max size is 100 and size is 100.'} |
| `qwen-3-32b` | text | ❌ `timeout` | 26.12s | Timeout limit exceeded |
| `qwen-3-4b` | text | ❌ `exception` | 4.81s | ResponseStatusError: Response 503: {'detail': 'Queue is full. Max size is 100 and size is 100.'} |
| `qwen-3-8b` | text | ❌ `timeout` | 26.58s | Timeout limit exceeded |
