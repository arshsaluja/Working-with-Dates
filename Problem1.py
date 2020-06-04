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
print(days_in_month(2019,6))#This is only for testing
