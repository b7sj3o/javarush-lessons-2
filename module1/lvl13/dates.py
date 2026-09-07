from datetime import datetime, date, time, timedelta, timezone

# dt = datetime(2026, 2, 25, 11, 20, 30)
# _time = time(1, 30, 25)
# _date = date(2026, 2, 28)
#
# td = timedelta(days=20)
#
# print(dt + td)
#

# user_input = input("Введіть ваше день народження у форматі: день.місяць.рік\n")
# day, month, year = map(int, user_input.split("."))
#
# dt = date(day=day, month=month, year=year)
#
# print(dt.strftime("Ти народився у: %A"))

dt = datetime(
    2026,
    2,
    25,
    11,
    20,
    30,
    tzinfo=timezone(timedelta(hours=-8))
)

print(dt)


dt.isoformat()                                # '2026-07-27T14:30:45'
datetime.fromisoformat("2026-07-27T14:30:45") # назад
date(2026, 7, 27).isocalendar()               # (year=2026, week=31, weekday=1)


from datetime import datetime, timezone
from zoneinfo import ZoneInfo

utc_now = datetime(2026, 7, 27, 12, 0, tzinfo=timezone.utc)

print(utc_now)                                    # 2026-07-27 12:00:00+00:00
print(utc_now.astimezone(ZoneInfo("Europe/Kyiv")))    # 15:00:00+03:00
print(utc_now.astimezone(ZoneInfo("Asia/Tokyo")))     # 21:00:00+09:00
print(utc_now.astimezone(ZoneInfo("Asia/Kathmandu"))) # 17:45:00+05:45