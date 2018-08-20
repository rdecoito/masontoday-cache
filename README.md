# masontoday-cache
Pulls the JSONs from masontoday and writes them to disk

#### Setting Up and Running the Project
1) Create a virtual environment with python3 and install the pip dependencies
    * `python3 -m venv venv` to create the venv
    * `source venv/bin/activate` to activate the venv
    * `pip3 install -r requirements.txt` to install the packages
2) With the venv activated, run `./start.sh` to activate the script
3) Now leave it! Check back every day to see the files in `logs/` appear!

#### Customising the Settings
In `scripts/mainscript.py`, you can customise the time at which cacheing is
done by modifying the `schedule.every().day.at("20:00").do(cache_sources)`
line. You can change the time in the `.at()` call with a string in 24-hour
clock format. If you'd like, you can also change the refresh rate in the while
loop by changing `sleep(3600)` to a time in seconds.