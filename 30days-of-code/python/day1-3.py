#!python3
print("--------------------------------------------------")
print("            Day 01 : datetime functions")
print("--------------------------------------------------")

from datetime import datetime
from datetime import date

#1:
print(datetime.today())
# 2020-04-02 13:02:34.423851

#2:
todaydate = date.today()
print(todaydate)
# 2020-04-02

#3:
day1 = date(2020, 9, 23)
print(day1)
# 2020-09-23

#4:
print(type(todaydate))
#<class 'datetime.date'>

#5:
print(todaydate.month)
#4

#6:
print(todaydate.year)
#2020

#7:
print(todaydate.day)
#2

#8:
christmas = date(2020, 12, 25)
print("This year, Christmas is on: {}".format(christmas))
# This year, Christmas is on: 2020-12-25

#9:
if christmas is not todaydate:
    print("Sorry there are still " + str((christmas - todaydate).days) + " until Christmas!")
else:
    print("Yay it's Christmas!")
