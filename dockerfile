FROM python:3.10.16-alpine

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

RUN pytest

CMD ["python", "monitor.py"]