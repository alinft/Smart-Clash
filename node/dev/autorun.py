import subprocess
import schedule
import time

def run_scripts():
    subprocess.call(['python', 'run_all.py'])

schedule.every(1).hours.do(run_scripts)

while True:
    schedule.run_pending()
    time.sleep(1)
