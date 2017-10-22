import datetime
import pytz

localTime = datetime.datetime.now()
utcTime = datetime.datetime.utcnow()

print("Naive local time {}".format(localTime))
print("Naive UTC {}".format(utcTime))

awareLocalTime = pytz.utc.localize(utcTime).astimezone()
awareUTCTime = pytz.utc.localize(utcTime)

print("Aware local time {}, time zone {}".format(awareLocalTime, awareLocalTime.tzinfo))
print("Aware UTC Time {}, time zone {}".format(awareUTCTime, awareUTCTime.tzinfo))

gap_time = datetime.datetime(2015, 10, 25, 1, 30, 0, 0)
print(gap_time)
print(gap_time.timestamp())

s = 1445733000
t = s + (60 * 60)

gb = pytz.timezone('GB')
dt1 = pytz.utc.localize(datetime.datetime.(s)).astimezone(gb)