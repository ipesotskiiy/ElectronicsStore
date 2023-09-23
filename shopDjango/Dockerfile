FROM python:3.8.12

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /shopDjango

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN chmod +x ./entrypoint.sh

RUN export && python manage.py collectstatic --noinput
CMD ["./entrypoint.sh"]
