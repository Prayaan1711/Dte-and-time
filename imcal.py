import calendar

obj = calendar.Calendar()

for x in obj.itermonthdays2(2012, 11):
    print(x)