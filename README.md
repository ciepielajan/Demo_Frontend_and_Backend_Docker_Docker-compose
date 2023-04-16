# ML_Streamlit_FastAPI_Docker
Deploying Machine Learning models with Streamlit, FastAPI and Docker

## install
```bash
sudo apt  install docker-compose
```

## run
```bash
docker-compose -f .\docker-compose.yml up
```

## bardzo ważne
Żeby frontend mógł się komunikować z backendem w pliku `docker-compose` contenerom trzeba nadać nazwy parametrem `container_name`. Jeżeli aplikacja frontendowa chce się połączyć z nią musi zrobić to przez url `http://container_name:PORT`.   Patrz plik `docker-compose.yml` -> `backend` -> `container_name` i `Streamlit_Frontend/app.py` zmienna `prediction_url`
