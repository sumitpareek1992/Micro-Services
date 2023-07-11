
FROM python:3.9

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN python3 -m pip install --upgrade pip

RUN pip3 install -r requirements.txt

COPY . /app

CMD python3 manage.py runserver 0.0.0.0:8001

EXPOSE 8001

