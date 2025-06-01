import calendar

cal = calendar.Calendar()

for x in cal.itermonthdates(2012, 11):
    print(x)
