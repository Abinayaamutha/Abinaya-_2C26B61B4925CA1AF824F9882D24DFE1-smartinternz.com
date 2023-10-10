
# Checking if the year is leap year
def leapyear(year):
  if year % 4 == 0 and year % 100 !=0:
    return True
  else:
    return false
year=1984
if leapyear(year):
  print("{} is a leap year".format(year))
else:
  print("{} is not a leap year".format(year))


