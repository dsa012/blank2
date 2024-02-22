import requests
import time
import random


for i in range(10):
    location = random.choice(['London', 'New York', 'California'])
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid=c54bf3918a2805b5d4c8e4b592e3ee76")
    print(i)
    time.sleep(10)