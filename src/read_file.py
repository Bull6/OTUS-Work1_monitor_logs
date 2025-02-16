import os

def read_log_file():
  log_file = os.environ.get('PATH_TO_NGINX_ACCESS_LOG', 'access.log')
  return log_file
