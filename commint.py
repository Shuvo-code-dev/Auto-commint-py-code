import os
import datetime

# পরিবর্তনযোগ্য ফাইলের নাম
file_path = "daily_update.txt"

# প্রতিদিনের নতুন তথ্য যোগ করা
with open(file_path, "a") as file:
    file.write(f"Updated on: {datetime.datetime.now()}\n")

# GitHub এ কমিট ও পুশ করা
os.system("git add .")
os.system('git commit -m "Daily update: ' + str(datetime.datetime.now()) + '"')
os.system("git push origin main")