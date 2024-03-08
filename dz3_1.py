#завдання 1
from datetime import datetime as dt
from datetime import datetime, timedelta





# #завдання 1 (виправив)
def get_days_from_today(date):
    
    try:
        inputDate = dt.strptime(date, '%Y-%m-%d')
        currentDate = dt.now()
        delta = currentDate - inputDate
        
        return delta.days

    except:
        return ValueError

print(get_days_from_today('2007-09-17'))