import time
from datetime import datetime, timedelta
import requests

SECRET_KEY = "YOUR_SECRET_KEY"  # 쿨SMS 시크릿키
TO_PHONE_NUMBER = "수신자 번호"  # 수신자 전화번호
FROM_PHONE_NUMBER = "발신자 번호"  # 발신자 전화번호

def send_sms(message):
    url = "https://api.coolsms.co.kr/sms/1.5/send"
    data = {
        "api_key": SECRET_KEY,
        "message": message,
        "to": TO_PHONE_NUMBER,
        "from": FROM_PHONE_NUMBER,
    }
    response = requests.post(url, data=data)
    if response.status_code == 200:
        print("SMS sent successfully")
    else:
        print("Failed to send SMS")

def is_holiday():
    today = datetime.today().date()
    weekday = today.weekday()
    if weekday == 5 or weekday == 6: 
        return True
    return False

def get_next_scheduled_time():
    current_time = datetime.now().time()
    scheduled_time = datetime.combine(datetime.today(), datetime.strptime("18:00", "%H:%M").time())
    if current_time >= scheduled_time:
        scheduled_time += timedelta(days=1)
    return scheduled_time

while True:
    scheduled_time = get_next_scheduled_time()
    current_time = datetime.now().time()
    
    if current_time >= scheduled_time.time() and not is_holiday():
        message = "저녁 6시입니다."
        send_sms(message)
    
    time.sleep(60)