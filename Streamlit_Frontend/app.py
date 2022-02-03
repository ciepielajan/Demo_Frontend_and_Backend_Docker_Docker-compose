import streamlit as st
import requests

data = {
    "value": "HC1:6BFC80Z80T9WTWGVLK659A:TG4G$BTZM0X*4FBBE*3FN0KKC+H3WY0/9CWC4*70 6AD97TK0F90KECTHGXJC$+D.JCBECB1A-:8$966469L6OF6VX6Z/ER2DD46JH8946XJCCWENF6OF63W5NW60A6WJCT3E 6AWJC0FDTA6AIA%G7X+AQB9746XG7TS9 967:6DL6WX8BM8CA6DB83R63X6$A7UF6QG8Q46/A8.A8$96V47.JCP9EJY8L/5M/5 96.96WF6%JCXQEIN8G/D6LE ZDQZCAJB0LEE4F0ECKQEPD09WEQDD+Q6TW6FA7C46TPCBEC8ZKW.CHWEBIAG09:S9Q+9DN90S7BIAOT9W.CUEEY3EAECWGDMXG2QDUW5*MEWUMMPCG/D8EDETAG+9*NAWB8 JC6/DYOACEC+EDR/OLEC$PC5$CUZCY$5Y$5JPCT3E5JDKA7Q47%964W5WA6N68$E5FAWIBG9SQCLEH19FZMD8B TL6AW8JJRBHTB91L0GMSNRCBBPL8R958CR2:7T84H7*6C V86W0*8G1MZJVS72L:M5WAB9UB0HF0",
}

# prediction_url = "http://127.0.0.1:8000/prediction"
prediction_url = "http://fastapi:8000/prediction"

st.write("http://fastapi - 3")

hall_response = requests.post(url=prediction_url, json={"data": data})
st.write(f"{hall_response.status_code},\n{hall_response.ok}")
if hall_response.ok:
    st.write("Output:")
    hall_response = hall_response.json()
    st.write(hall_response)
else:
    st.write(f"{hall_response.json().get('detail')}")

