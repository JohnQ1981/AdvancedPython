def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        print("Leap year.")
        return True
      else:
        print("Not leap year.")
        return False
    else:
      print("Leap year.")
      return True
  else:
    print("Not leap year.")
    return False

def days_in_month(months):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if is_leap(year)  and months == 2:
    return 29
  # elif (is_leap == False and month ==2):
  #   return month_days[month-1]
  else:
    return month_days[month-1]


  
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(months=month)
print(days)
is_leap(year)







