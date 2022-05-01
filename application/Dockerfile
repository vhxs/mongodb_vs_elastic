FROM python:latest

ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=off

RUN pip install poetry gunicorn

WORKDIR /app
COPY poetry.lock pyproject.toml /app/
RUN poetry install
COPY . /app/

# this isn't working for some reason, not recognizing dependencies installed with poetry...
# CMD ["poetry", "run", "gunicorn", "--bind", "0.0.0.0:8080", "wsgi:app"]
CMD ["poetry", "run", "flask", "run", "--host=0.0.0.0"]