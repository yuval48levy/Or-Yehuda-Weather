import schedule
import time
from rabbitmq import send_to_rabbitmq
from weather import get_current_weather

def job():
    temp = get_current_weather()
    send_to_rabbitmq(temp)

def main():
    job()
    
    schedule.every(1).hours.do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
