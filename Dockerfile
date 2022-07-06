FROM python:3.9-slim-buster

COPY pyproject.toml pyproject.toml
COPY poetry.lock poetry.lock
COPY poetry.toml poetry.toml

RUN apt-get update && apt-get install -y curl
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:$PATH"
RUN poetry install

COPY . .

EXPOSE 5000
CMD [ "sh", "run.sh"]