# gpt4free-checker

[English Version (Английская версия)](README.md)

[![gpt4free-checker Models Online](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/LZTD1/gpt4free-checker/main/reports/badge.json)](https://github.com/LZTD1/gpt4free-checker/blob/main/reports/summary.md)

Автоматизированный, легковесный и отказоустойчивый диагностический инструмент, предназначенный для регулярного мониторинга работы API-провайдеров и проверки доступности моделей в библиотеке `gpt4free` (`g4f`).

## Фичи

* **Интеллектуальная сортировка моделей:** Автоматически распознает, связывает и группирует обнаруженные модели по четырем основным направлениям (**Текст**, **Изображение**, **Аудио**, **Видео**), основываясь на встроенных метаданных библиотеки `g4f`.
* **Отказоустойчивые тесты с ретраями:** Собственный параллельный раннер с жестким ограничением времени выполнения (глобальные таймауты), умной классификацией ошибок (лимиты запросов, таймауты, HTTP-коды) и настраиваемыми повторными попытками запросов.
* **Движок изменений (Diff):** Автоматически сравнивает показатели текущего прогона со вчерашними результатами и выводит список изменений.

## Отчеты и структура файлов

Все результаты тестирования автоматически сохраняются в папку `reports/` данного репозитория.

| Файл отчета / Путь | Описание и содержимое | Просмотр | Ссылка для парсеров (Raw) |
|--- |--- |:---:|:---:|
| ⭐ **`working.txt`** | **Главный файл.** Простой машиночитаемый плоский pipe-формат (`provider\|model\|capability\|time`) для быстрых автоматических bash-скриптов. | [Открыть](https://github.com/LZTD1/gpt4free-checker/blob/main/reports/working.txt) | [Raw URL](https://raw.githubusercontent.com/LZTD1/gpt4free-checker/main/reports/working.txt) |
| ⭐ **`working.json`** | **Главный файл.** Структурированный список всех проверенных активных моделей в виде стандартного JSON-массива. | [Открыть](https://github.com/LZTD1/gpt4free-checker/blob/main/reports/working.json) | [Raw URL](https://raw.githubusercontent.com/LZTD1/gpt4free-checker/main/reports/working.json) |
| **`summary.md`** | Главная панель для человека. Содержит общую статистику успешности, сводку по типам моделей и интерактивную таблицу провайдеров. | [Открыть](https://github.com/LZTD1/gpt4free-checker/blob/main/reports/summary.md) | [Raw URL](https://raw.githubusercontent.com/LZTD1/gpt4free-checker/main/reports/summary.md) |
| **`changes.md`** | Детализированный отчет изменений по сравнению с прошлым прогоном (что починилось, а что сломалось). | [Открыть](https://github.com/LZTD1/gpt4free-checker/blob/main/reports/changes.md) | [Raw URL](https://raw.githubusercontent.com/LZTD1/gpt4free-checker/main/reports/changes.md) |
| **`working_by_capability.json`** | Сгруппированный JSON-словарь, разделяющий рабочие модели по ключам: `text`, `image`, `audio`, `video`. | [Открыть](https://github.com/LZTD1/gpt4free-checker/blob/main/reports/working_by_capability.json) | [Raw URL](https://raw.githubusercontent.com/LZTD1/gpt4free-checker/main/reports/working_by_capability.json) |
| **`summary.json`** | Полная детальная статистика прогона, используемая скриптом для расчета изменений (diff). | [Открыть](https://github.com/LZTD1/gpt4free-checker/blob/main/reports/summary.json) | [Raw URL](https://raw.githubusercontent.com/LZTD1/gpt4free-checker/main/reports/summary.json) |
| **`reports/providers/`** | Папка с индивидуальными Markdown-отчетами (`<ИмяПровайдера>.md`) для каждого провайдера. Содержит таблицу моделей с их типами, статусом тестирования, временем отклика, причинами ошибок и примерами сырых ответов моделей. | [Открыть](https://github.com/LZTD1/gpt4free-checker/blob/main/reports/providers/) | [Raw Папка](https://raw.githubusercontent.com/LZTD1/gpt4free-checker/main/reports/providers/) |