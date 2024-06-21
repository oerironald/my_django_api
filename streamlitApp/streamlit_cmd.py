import subprocess

def run_streamlit_app():
    subprocess.run(["streamlit", "run", "streamlit_app.py"])

def handle(*args, **options):
    run_streamlit_app()
