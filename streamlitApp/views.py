import subprocess
from django.shortcuts import render

def streamlit_app(request):
    # Run the Streamlit application
    subprocess.Popen(["streamlit", "run", "/workspaces/my_django_api/streamlitApp/streamlit_app.py"])
    return render(request, 'streamlitApp/streamlit.html')