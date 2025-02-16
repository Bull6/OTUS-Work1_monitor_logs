import pandas as pd
from statistics import mean, median

# Функция для ручного парсинга логов
def parse_log_line(line):
    """Парсит строку лога Nginx вручную."""
    parts = line.split()
    if len(parts) < 12:
        return None
    
    # Извлекаем поля и удаляем кавычки
    ip = parts[0]
    timestamp = parts[3] + " " + parts[4].strip("[]")  # Убираем квадратные скобки
    request = " ".join(parts[5:8]).strip('"')  # Удаляем кавычки
    status = parts[8]
    size = parts[9]
    referrer = parts[10].strip('"')  # Удаляем кавычки
    user_agent = " ".join(parts[11:-1]).strip('"')  # Удаляем кавычки
    request_time = parts[-1]
    
    return {
        'ip': ip,
        'timestamp': timestamp,
        'request': request,
        'status': status,
        'size': size,
        'referrer': referrer,
        'user_agent': user_agent,
        'request_time': request_time
    }

def read_logs_with_pandas(log_file):
    """Читает логи Nginx и возвращает DataFrame."""
    data = []
    
    with open(log_file, 'r') as file:
        for line in file:
            parsed_data = parse_log_line(line)
            if parsed_data:
                data.append(parsed_data)
    
    # Создаем DataFrame
    df = pd.DataFrame(data)
    
    # Очищаем данные
    df['request_time'] = df['request_time'].astype(float)
    df['status'] = df['status'].astype(int)
    df['size'] = df['size'].astype(int)
    
    return df

def calculate_statistics(log_file):
    """Вычисляет статистику на основе логов."""
    df = read_logs_with_pandas(log_file)
    
    if df.empty:
        return None
    
    request_times = df['request_time'].tolist()
    
    avg_time = mean(request_times)
    median_time = median(request_times)
    
    return {
        'average_response_time': avg_time,
        'median_response_time': median_time,
        'total_requests': len(request_times)
    }

def generate_report(stats):
    """Генерирует отчет на основе статистики."""
    if not stats:
        return "No data to generate report."
    
    report = (
        f"Total Requests: {stats['total_requests']}\n"
        f"Average Response Time: {stats['average_response_time']:.4f} seconds\n"
        f"Median Response Time: {stats['median_response_time']:.4f} seconds\n"
    )
    return report

