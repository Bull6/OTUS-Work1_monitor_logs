import pytest
from src.monitor import parse_log_line  # Импортируем функцию для тестирования

# Пример тестовых данных
valid_log_line = '127.0.0.1 - - [10/Oct/2023:13:55:36 +0000] "GET /example HTTP/1.1" 200 612 "-" "curl/7.68.0" 0.002'
invalid_log_line = 'invalid log line'

def test_parse_log_line_valid():
    """Тест для проверки парсинга валидной строки лога."""
    result = parse_log_line(valid_log_line)
    assert result is not None
    assert result['ip'] == '127.0.0.1'
    assert result['request'] == 'GET /example HTTP/1.1'
    assert result['status'] == '200'
    assert result['request_time'] == '0.002'

def test_parse_log_line_invalid():
    """Тест для проверки парсинга невалидной строки лога."""
    result = parse_log_line(invalid_log_line)
    assert result is None