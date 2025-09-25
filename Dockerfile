FROM python:3.12-slim
ENV PYTHONDONTWRITEBYTECODE=1
WORKDIR /app
RUN pip install --upgrade pip pipenv
COPY Pipfile Pipfile.lock /app/
RUN pipenv install --deploy --ignore-pipfile
COPY . .
EXPOSE 5005
CMD ["pipenv", "run", "flask", "run", "--host", "0.0.0.0"]






