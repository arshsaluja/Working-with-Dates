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
    c=0
    if year>=datetime.MINYEAR and year<=datetime.MAXYEAR and month>=1 and month<=12 and day>=1 and day<=days_in_month(year, month):
        return True
    else:
        return False
print(days_in_month(2019,6))#This is only for testing
print(is_valid_date(2019,12,31)) #This is only for testing
