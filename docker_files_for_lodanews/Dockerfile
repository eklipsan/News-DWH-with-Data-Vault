FROM python:3.10
WORKDIR /app
ENV TABLE_NAME=News
COPY countries.py main.py loadtran.py requirements.txt /app
RUN pip install --upgrade pip && pip install -r requirements.txt && mkdir log_news
CMD ["python", "main.py"]
