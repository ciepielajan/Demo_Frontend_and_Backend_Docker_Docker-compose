# # backend/Dockerfile

# FROM python:3.9
# COPY requirements.txt app/requirements.txt
# WORKDIR /app
# RUN pip install -r requirements.txt
# COPY . /app
# EXPOSE 8000
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000" , "--reload"]
# CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8000", "main:app"]

FROM python:3.8-slim-buster
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 8000
CMD exec uvicorn main:app --host 0.0.0.0 --port 8000 --reload
# CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 app:app