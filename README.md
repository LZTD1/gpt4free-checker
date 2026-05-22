# gpt4free-checker

[Русская версия (Russian Version)](README.RU.md)

[![gpt4free-checker Models Online](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/LZTD1/gpt4free-checker/main/reports/badge.json)](https://github.com/LZTD1/gpt4free-checker/blob/main/reports/summary.md)

An automated, lightweight, and resilient diagnostic test suite designed to monitor and verify active `gpt4free` (`g4f`) API providers and model availability.

## Features

* **Intelligent Model Classification & Sorting:** Automatically detects, maps, and filters discovered models into distinct categories (**Text**, **Image**, **Audio**, **Video**) using native `g4f` metadata, avoiding unreliable string-matching hacks.
* **Fail-safe Testing with Retries & Timeouts:** Implements a custom parallel runner with global timeouts, smart exception classification (timeouts, rate limits, HTTP codes), and automatic backoff retries.
* **Daily Change Engine (Diff):** Automatically compares current test results with the previous run to generate a clear changelog.

## Reports & Artifacts

All generated reports are saved in the `reports/` directory of this repository.

| Report File / Path | Purpose & Contents | GitHub View | Raw Parser Link |
|--- |--- |:---:|:---:|
| ⭐ **`working.txt`** | **Core File.** Compact, machine-readable flat pipe-separated format (`provider\|model\|capability\|time`) for fast automation scripts. | [View](https://github.com/LZTD1/gpt4free-checker/blob/main/reports/working.txt) | [Raw URL](https://raw.githubusercontent.com/LZTD1/gpt4free-checker/main/reports/working.txt) |
| ⭐ **`working.json`** | **Core File.** Structured list of all verified working models in standard JSON array format. | [View](https://github.com/LZTD1/gpt4free-checker/blob/main/reports/working.json) | [Raw URL](https://raw.githubusercontent.com/LZTD1/gpt4free-checker/main/reports/working.json) |
| **`summary.md`** | Main human-readable dashboard. Displays overall success rate, statistics by capability, and an interactive status table of all providers. | [View](https://github.com/LZTD1/gpt4free-checker/blob/main/reports/summary.md) | [Raw URL](https://raw.githubusercontent.com/LZTD1/gpt4free-checker/main/reports/summary.md) |
| **`changes.md`** | Detailed changelog comparing current results to the previous run (Newly working / Newly broken models). | [View](https://github.com/LZTD1/gpt4free-checker/blob/main/reports/changes.md) | [Raw URL](https://raw.githubusercontent.com/LZTD1/gpt4free-checker/main/reports/changes.md) |
| **`working_by_capability.json`** | Grouped JSON dictionary mapping working models inside four primary keys: `text`, `image`, `audio`, `video`. | [View](https://github.com/LZTD1/gpt4free-checker/blob/main/reports/working_by_capability.json) | [Raw URL](https://raw.githubusercontent.com/LZTD1/gpt4free-checker/main/reports/working_by_capability.json) |
| **`summary.json`** | Comprehensive metrics payload used for diff calculations. | [View](https://github.com/LZTD1/gpt4free-checker/blob/main/reports/summary.json) | [Raw URL](https://raw.githubusercontent.com/LZTD1/gpt4free-checker/main/reports/summary.json) |
| **`reports/providers/`** | Individual directory containing markdown reports (`<ProviderName>.md`) for each provider. Features exact test logs, response times, error reasons for failed checks, and raw sample preview outputs for working models. | [Browse](https://github.com/LZTD1/gpt4free-checker/blob/main/reports/providers/) | [Raw Folder](https://raw.githubusercontent.com/LZTD1/gpt4free-checker/main/reports/providers/) |