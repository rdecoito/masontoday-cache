from requests import get
import schedule
import datetime
from time import sleep



# def cache_the_cache():
    # 25live = get("https://masontoday.gmu.io/api/25live").text
    # getconn = get("https://masontoday.gmu.io/api/getconnected").text


with open("../logs/MasonTodayLog_" + str(datetime.date.today()) + ".txt",
          "w") as file:
    file.write(get("https://masontoday.gmu.io/api/25live").text)

print("Woah, we did it!")
