import base64
from django.conf import settings

def generate_password(date):
    data_to_encode = settings.BUSINESS_SHORT_CODE + settings.LIPANAMPESA_PASSKEY + date
    encoded_string = base64.b64encode(data_to_encode.encode("utf-8"))
    decoded_pass = encoded_string.decode("utf-8")

    return decoded_pass