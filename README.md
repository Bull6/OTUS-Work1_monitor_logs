# Nginx Log Monitor

Сервис для мониторинга и анализа логов Nginx. Проект предоставляет статистику по запросам, такую как среднее время ответа, медианное время ответа и 95-й перцентиль.

## Основные функции

- Парсинг логов Nginx.
- Расчет статистики:
  - Среднее время ответа.
  - Медианное время ответа.
  - Кол-во запросов.
- Поддержка Docker для удобного развертывания.
- Интеграция с GitHub Actions для автоматического тестирования и сборки.

## Использование

### Запуск вручную

1. Укажите путь до файла в переменной окружения ```PATH_TO_NGINX_ACCESS_LOG``` -- значение по-умолчанию ```access.log```.
2. Запустите скрипт:

   ```bash
   python run.py
   ```

   Скрипт начнет мониторить файл логов и выводить статистику .

### Запуск через Docker

1. Соберите Docker-образ:

   ```bash
   docker build -t image-name .
   ```

2. Запустите контейнер, указав путь к вашему файлу логов:

   ```bash
   docker run -v /path/to/your/access.log:/app/access.log image-name
   ```

   Замените `/path/to/your/access.log` на путь к вашему файлу `access.log`.

## Тестирование

Проект включает тесты, написанные с использованием `pytest`. Чтобы запустить тесты:

```bash
pytest
```

Для измерения покрытия кода тестами используйте:

```bash
pytest --cov=monitor --cov-report=html
```

Отчет о покрытии будет доступен в директории `htmlcov`.

## GitHub Actions

Проект настроен для автоматического тестирования и сборки через GitHub Actions. При каждом пуше в ветку `main` или создании pull request:

1. Устанавливаются зависимости.
2. Запускаются тесты.
3. Собирается Docker-образ.
4. Docker-образ публикуется в Docker Hub (если настроены секреты).

