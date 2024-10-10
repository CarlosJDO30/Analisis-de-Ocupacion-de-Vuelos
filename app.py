import streamlit as st

# Título del Dashboard
st.title("Dashboard de Power BI en Streamlit")

# Incrustar el dashboard de Power BI usando un iframe
power_bi_url = "https://app.powerbi.com/view?r=eyJrIjoiNTEzM2M3MjQtNDE2ZS00OTc2LTk5ZDEtZDg1OWUyZmRjZmIwIiwidCI6Ijk4YjVlNzlkLWEwODYtNGU3OC04NDUxLTgxMmE3MGM0NWRlNyIsImMiOjR9&pageName=ee96d4157dfda6adb7a8"

st.components.v1.iframe(src=power_bi_url, width=800, height=600)
