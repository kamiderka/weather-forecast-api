FROM python:3.12.3

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./src /code/src

EXPOSE 8080

CMD ["fastapi", "run", "src/main.py", "--port", "8080"]