
# logger.py — logs user activity to CSV
import datetime
import csv

def log_event(team, opponent, count):
    with open("user_log.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([datetime.datetime.now().isoformat(), team, opponent, count])
