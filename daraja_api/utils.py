from datetime import datetime

def timestamp_conversion():
    unformatted_time = datetime.now()
    formatted_time = unformatted_time.strftime("%Y%d%H%M%S")

    return formatted_time