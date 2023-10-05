FROM python:3.9.13-slim-buster
ENV DOCKER_BUILDKIT=1

WORKDIR /app

ENV POETRY_VERSION=1.3.2
RUN python3 -m pip install poetry==$POETRY_VERSION

COPY pyproject.toml poetry.lock ./
RUN poetry config virtualenvs.create false

COPY ./athena /app/

RUN poetry install --no-interaction --no-ansi --without dev

CMD ["python", "main.py"]
