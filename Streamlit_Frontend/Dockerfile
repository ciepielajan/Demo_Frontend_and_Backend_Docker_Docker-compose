# frontent/Dockerfile

# FROM python:3.9
# COPY requirements.txt app/requirements.txt
# WORKDIR /app
# RUN pip install -r requirements.txt
# COPY . /app
# EXPOSE 8501
# ENTRYPOINT ["streamlit","run"]
# CMD ["app.py"]

FROM python:3.8-slim-buster
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 8501
ENTRYPOINT streamlit run --server.port 8501 app.py