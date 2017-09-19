# Dependencies
import datetime, time, pytz
from tzlocal import get_localzone

local_tz = get_localzone()
timezone = pytz.timezone("US/Eastern")
today = datetime.datetime.today()
now = datetime.datetime.now()

dt = today.strftime('%m/%d/%y')
dt1 = today.strftime('%m-%d-%y')

# curtime = now.strftime('%m-%d-%y %H:%M:%S')
# curtime30 = now + datetime.timedelta(minutes = 5)

# print(curtime)
# while(True):
#     # print((datetime.datetime.now() + datetime.timedelta(minutes = 1)).strftime('%m-%d-%y %H:%M:%S'))
#     # print("sleeping till EST.." + (datetime.datetime.now() + datetime.timedelta(minutes = 1)).strftime('%m-%d-%y %H:%M:%S'))
#     # print("sleeping till UTC.." + (datetime.datetime.now().replace(tzinfo=True).astimezone(tz=timezone) + datetime.timedelta(minutes = 1)).strftime('%m-%d-%y %H:%M:%S'))
#     # print("sleeping till PST.." + (datetime.datetime.now().replace(tzinfo=datetime.timezone.utc).astimezone(tz=None) + datetime.timedelta(minutes = 1)).strftime('%m-%d-%y %H:%M:%S'))
#     ts = time.time()
#     utc_now, now = datetime.datetime.utcfromtimestamp(ts), datetime.datetime.fromtimestamp(ts)
#     local_now = utc_now.replace(tzinfo=pytz.utc).astimezone(local_tz)
#     local_now_pytz_tz = utc_now.replace(tzinfo=pytz.utc).astimezone(timezone)
#     print("ts:", ts)
#     print("utc_now", utc_now)
#     print("now: ", now)
#     print("local_now", now)
#     print("")
#     time.sleep(60)

ts = time.time()
utc_now, now = datetime.datetime.utcfromtimestamp(ts), datetime.datetime.fromtimestamp(ts)
local_now = utc_now.replace(tzinfo=pytz.utc).astimezone(local_tz)
local_now_pytz_tz = utc_now.replace(tzinfo=pytz.utc).astimezone(timezone)
print("ts:", ts)
print("utc_now", utc_now)
print("now: ", now)
print("local_now", now)
print("local_now_pytz_tz", local_now_pytz_tz)