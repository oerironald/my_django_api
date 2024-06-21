import streamlit as st
import requests


@st.cache
def fetch_covid_data():
    url = "https://disease.sh/v3/covid-19/all"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def main():
    data = fetch_covid_data()
    if data:
        st.json(data)
    else:
        st.error("Failed to fetch COVID-19 data")

if __name__ == "__main__":
    main()
