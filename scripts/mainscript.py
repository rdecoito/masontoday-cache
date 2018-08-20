# python imports
import datetime
import os
from time import sleep

# package imports
from requests import get
import schedule


# current working directory
currentdir = os.getcwd()

# all the current MasonToday sources in format (filename, URL)
sources = [
    ("25Live", "https://masontoday.gmu.io/api/25live"),
    ("GetConn", "https://masontoday.gmu.io/api/getconnected")
]


def cache_sources():
    for source in sources:
        path = os.path.join(currentdir + "/logs/MasonTodayLog_" + source[0] \
                                + "_" + str(datetime.date.today()) + ".txt")
        with open(path, "a") as file:
            file.write(str(get(source[1]).text))
            file.close()
        print(source[0] + " cache successful!")


# cache the sources at 8 PM every day
schedule.every().day.at("20:00").do(cache_sources)

do_it = True
while (do_it):
    schedule.run_pending()
    sleep(3600)  # check every hour