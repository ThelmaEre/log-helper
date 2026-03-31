import base64
import csv
from datetime import datetime

log_file = "logs/auth_log.csv"

failed_logins = {}

with open(log_file, "r") as file:
    reader = csv.reader(file)

    header = next(reader)
    print(header)

    for row in reader:
        timestamp, username, ip, action = row
        #try decoding base64 actions
        try:
            decoded = base64.b64decode(action).decode("utf-8")
            print(f"🕵️ Encoded command detected: {decoded}")
        except:
            pass

            

        # convert timestamp
        utc_time = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%SZ")
        readable_time = utc_time.strftime("%Y-%m-%d %I:%M:%S %p")

        # track failed logins
        if action == "LOGIN_FAILED":
            failed_logins[username] = failed_logins.get(username, 0) + 1

        # check if success after failures
        elif action == "LOGIN_SUCCESS":
            if failed_logins.get(username, 0) >= 2:
                print(f"⚠️ Suspicious login detected for {username} at {readable_time}")

            failed_logins[username] = 0

        print([readable_time, username, ip, action])

import os

evidence_folder = "evidence"

files = os.listdir(evidence_folder)

for index, filename in enumerate(files, start=1):
    old_path = os.path.join(evidence_folder, filename)

    new_name = f"case001_evidence_{index}.txt"
    new_path = os.path.join(evidence_folder, new_name)

    os.rename(old_path, new_path)
    print(f"Renamed {filename} → {new_name}")
