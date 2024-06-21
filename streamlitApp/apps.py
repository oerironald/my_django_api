from django.apps import AppConfig
from django.conf import settings
import threading

class YourAppConfig(AppConfig):
    name = 'streamlitApp'

    def ready(self):
        # Run the management command in a separate thread
        thread = threading.Thread(target=self.start_streamlit_app)
        thread.start()

    def start_streamlit_app(self):
        from django.core.management import call_command
        call_command('streamlit_app_command')
