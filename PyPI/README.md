tiny-text-stats — это небольшая учебная библиотека для подсчета простых характеристик текста. Я выбрал такую идею, потому что ее легко проверить. Функция принимает строку и возвращает количество символов, слов и строк.

Ссылки:  
GitHub:  [https://github.com/xx663xx/repo](https://github.com/xx663xx/repo)  
TestPyPI:  [https://test.pypi.org/project/tiny-text-stats-2026/](https://test.pypi.org/project/tiny-text-stats-2026/)

Что делает библиотека?
В пакете есть функция analyze_text. Она возвращает объект TextStats с тремя полями - characters, words и lines. Это соответственно количество символов, слов и строк.

Пример использования:

```python
from tiny_text_stats import analyze_text

stats = analyze_text("hello world\nagain")
print(stats.words)

```

Структура проекта выглядит так:

```
PyPI/
├── Makefile
├── README.md
├── pyproject.toml
├── setup.py
├── src/
│   └── tiny_text_stats/
│       ├── __init__.py
│       ├── core.py
│       └── py.typed
└── tests/
    └── test_core.py

```

Файл setup.py содержит описание пакета. Там указаны имя, версия, автор, ссылка на GitHub, зависимости и настройки для поиска модулей в папке src.  
Файл pyproject.toml нужен для сборки, он говорит, какие инструменты использовать.

Проверка через Make  
Все основные команды вынесены в Makefile, чтобы не запускать их вручную.

```
make install
make lint
make type
make test
make docs
make build

```

Есть общий таргет:

```
make check

```

Он запускает все проверки сразу, включая стиль, типы, тесты, документацию и сборку.

Установка из TestPyPI  
После публикации пакет можно установить так:

```
pip install --index-url https://test.pypi.org/simple/ tiny-text-stats-2026

```

Для публикации есть отдельная команда:

```
make publish-testpypi

```
