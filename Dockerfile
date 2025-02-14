FROM python:3.6

WORKDIR /usr/src/app

COPY ./app/ /usr/src/app

RUN pip install pipenv
RUN pipenv install

ENV PIPENV_DONT_LOAD_ENV=1
ENV PYTHONUNBUFFERED=1

EXPOSE 80/tcp

ENTRYPOINT ["pipenv", "run", "python", "landerr.py"]