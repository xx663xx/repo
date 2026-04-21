# Монорепозиторий FOSSDEV

В этой ветке находится отдельное решение задания про упаковку Python-проекта и публикацию
на TestPyPI. Старые задания лежат в своих ветках и здесь специально не смешиваются.

## Где находится работа

Основной каталог проекта:

- [`PyPI/README.md`](PyPI/README.md) — описание идеи, структуры и проверки;
- [`PyPI/Makefile`](PyPI/Makefile) — автоматизация команд;
- [`PyPI/setup.py`](PyPI/setup.py) — настройки сборки пакета;
- [`PyPI/src/tiny_text_stats/`](PyPI/src/tiny_text_stats/) — исходный код библиотеки;
- [`PyPI/tests/`](PyPI/tests/) — простые тесты.

## Короткая инструкция для проверки

```bash
cd PyPI
make install
make check
make build
```

После публикации пакет должен устанавливаться из TestPyPI так:

```bash
pip install --index-url https://test.pypi.org/simple/ tiny-text-stats-2026
```

Ссылка на страницу проекта в TestPyPI указана в README внутри каталога `PyPI`.
