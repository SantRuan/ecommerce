FROM python:3.9

WORKDIR /src

COPY Pipfile Pipfile.lock ./

RUN pip install --no-cache-dir pipenv && \
    pipenv install --deploy --ignore-pipfile

COPY /src .

EXPOSE 8000 


CMD ["pipenv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]


