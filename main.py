import time
from mailer import send_notification
from daytime_api_config import is_night
from iss_api_config import checking_iss_position

while True:
    time.sleep(200)
    send_notification(is_night=is_night(), iss_position=checking_iss_position())
