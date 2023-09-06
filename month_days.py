#My code
#Calculating leap year

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))

def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
     return True
  else:
    return False
year_result = is_leap(year)    

def days_in_month(chosen_year, chosen_month):
  day_picked = ""
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if chosen_year == False in year_result:
    day_picked = month_days[chosen_month -1]
  else:
    month_days[1] = 29
    day_picked = month_days[chosen_month -1]
  return day_picked  


days = days_in_month(year, month)
print(days)

#Teacher code

def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
     return True
  else:
    return False

def days_in_month(chosen_year, chosen_month):
  if chosen_month > 12 or chosen_month < 1:
    return "Invalid month"
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if is_leap(year) and chosen_month == 2:
    return 29
  return month_days[chosen_month -1]  

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
