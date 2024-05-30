FROM python:3.12.3

WORKDIR /django

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

COPY requirement2.txt requirement2.txt

RUN pip3 install -r requirement2.txt

COPY  . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
