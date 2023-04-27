# ML_Streamlit_FastAPI_Docker
Deploying Machine Learning models with Streamlit, FastAPI and Docker

## install
```bash
sudo apt  install docker-compose
```

## run
```bash
docker-compose up
# jeżli jakiś obraz już istnieje to napisz go / skakuj i zbuduj na nowo 
docker-compose up -bulid
# lub force 
docker-compose up -bulid -f
```

## bardzo ważne
Żeby frontend mógł się komunikować z backendem w pliku `docker-compose` contenerom trzeba nadać nazwy parametrem `container_name`. Jeżeli aplikacja frontendowa chce się połączyć z nią musi zrobić to przez url `http://container_name:PORT`.   Patrz plik `docker-compose.yml` -> `backend` -> `container_name` i `Streamlit_Frontend/app.py` zmienna `prediction_url`


## Info o Docker

https://github.com/ciepielajan/docker_start
