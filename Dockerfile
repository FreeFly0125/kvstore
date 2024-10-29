FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt ./

RUN --mount=type=cache,target=/root/.cache/pip pip3 install -r requirements.txt

COPY . .

EXPOSE 4000

CMD [ "uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "4000" ]