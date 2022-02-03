import streamlit as st
import requests


data_test = {
    "Hello": "World",
}


# prediction_url = "http://127.0.0.1:8000/prediction"
prediction_url = "http://fastapi:8000/prediction"

st.write("fastapi - v10")

hall_response = requests.post(url=prediction_url, json=data_test)

st.write(f"{hall_response.status_code},\n{hall_response.ok}")
if hall_response.ok:
    st.write("Output:")
    hall_response = hall_response.json()
    st.write(hall_response)
else:
    st.write(f"{hall_response.json().get('detail')}")
