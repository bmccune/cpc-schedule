def get_current_day():
    from datetime import datetime
    return datetime.now().strftime("Todays Day:%b %d")

def get_current_time():
    from datetime import datetime
    return datetime.now().strftime("%X")