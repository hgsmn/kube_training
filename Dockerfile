FROM python:3.12-alpine

ENV PYTHONUNBUFFERED 1
# We disable bytecode generation for cleaner build
ENV PYTHONDONTWRITEBYTECODE 1

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt 

WORKDIR /app

COPY . .

CMD ["uvicorn", "app.app:app", "--root-path", "/api","--reload", "--host", "0.0.0.0", "--port" , "8100"]
