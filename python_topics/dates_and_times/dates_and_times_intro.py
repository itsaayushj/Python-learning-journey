import datetime 

date = datetime.date(2026 , 9 , 19)
date_today = datetime.date.today()

print(date)
print(date_today)

time = datetime.time(4 , 9, 42)
time_now_raw = datetime.datetime.now()
time_now = time_now_raw.strftime("%H:%M:%S")
full_date_and_time = time_now_raw.strftime("%d-%m-%Y//%H:%M:%S")
print(time)
print(time_now_raw)
print(time_now)
print(full_date_and_time)




