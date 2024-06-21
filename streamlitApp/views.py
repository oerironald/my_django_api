from django.shortcuts import render
import requests

def streamlit_view(request):
    # Make a request to the Streamlit app's endpoint to fetch COVID-19 data
    print("Fetching data from Streamlit app...")
    response = requests.get("http://localhost:8501/")  # Replace with the appropriate URL
    if response.status_code == 200:
        print("Data fetched successfully.")
        data = response.json()
        print("Data:", data)
        # Process the data and return a response
        return render(request, 'streamlitApp/streamlit.html', {'data': data})
    else:
        print("Failed to fetch data.")
        # Handle error
        return render(request, 'error_template.html')
