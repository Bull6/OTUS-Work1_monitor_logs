import src.monitor as monitor
import src.read_file as log_file

# Пример использования
stats = monitor.calculate_statistics(log_file.read_log_file())
report = monitor.generate_report(stats)

print(report, end='')