import datetime
def days_in_month(year, month):
    """
    Inputs:
      year  - an integer between datetime.MINYEAR and datetime.MAXYEAR
              representing the year
      month - an integer between 1 and 12 representing the month
      
    Returns:
      The number of days in the input month.
    """
    d1=datetime.date(year,month,1)
    if month==12:
        d2=datetime.date(year+1,1,1)
    else:
        d2=datetime.date(year,month+1,1)
    d=d2-d1
    return d.days
def is_valid_date(year, month, day):
    """
    Inputs:
      year  - an integer representing the year
      month - an integer representing the month
      day   - an integer representing the day
      
    Returns:
      True if year-month-day is a valid date and
      False otherwise
    """
    if year>=datetime.MINYEAR and year<=datetime.MAXYEAR and month>=1 and month<=12 and day>=1 and day<=days_in_month(year, month):
        return True
    else:
        return False
def days_between(year1, month1, day1, year2, month2, day2):
    """
    Inputs:
      year1  - an integer representing the year of the first date
      month1 - an integer representing the month of the first date
      day1   - an integer representing the day of the first date
      year2  - an integer representing the year of the second date
      month2 - an integer representing the month of the second date
      day2   - an integer representing the day of the second date
      
    Returns:
      The number of days from the first date to the second date.
      Returns 0 if either date is invalid or the second date is 
      before the first date.
    """
    d1=datetime.date(year1, month1, day1)
    d2=datetime.date(year2, month2, day2)
    d=d2-d1
    e=d.days
    if is_valid_date(year1, month1, day1) and is_valid_date(year2, month2, day2) and d2>d1:
        return e
    else:
        return 0
def age_in_days(year, month, day):
    """
    Inputs:
      year  - an integer representing the birthday year
      month - an integer representing the birthday month
      day   - an integer representing the birthday day
      
    Returns:
      The age of a person with the input birthday as of today.
      Returns 0 if the input date is invalid of if the input
      date is in the future.
    """
    d1=datetime.date(year,month,day)
    d2=datetime.date.today()
    t=days_between(year,month,day,d2.year,d2.month,d2.day)
    if is_valid_date(year, month, day) and d1<=d2:
        return t
    else:
        return 0

print(days_in_month(2019,6))#This is only for testing
print(is_valid_date(2019,12,31)) #This is only for testing
print(days_between(2019,12,3,2020,1,31))#This is only for testing
print(age_in_days(2000,6,16))#This is only for testing
