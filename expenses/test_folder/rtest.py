from datetime import datetime
import pytz

timezone = pytz.timezone('Asia/Samarkand')
date_s = datetime.now(timezone)
year = date_s.year
month = date_s.month
day = date_s.day
print(date_s.year)