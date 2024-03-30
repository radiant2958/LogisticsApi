
FROM python:3.11

WORKDIR /usr/src/app

COPY wait-for-it.sh /wait-for-it.sh
RUN chmod +x /wait-for-it.sh

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .


CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
