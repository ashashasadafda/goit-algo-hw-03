# завдання 4
from datetime import datetime as dt
from datetime import datetime, timedelta

def get_upcoming_birthdays(users) -> list:
    today = datetime.today().date()
    
    upcoming_birthdays = []
    
    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        
        next_birthday_year = today.year
        
        # if birthday < today:
        #     next_birthday_year += 1
        
        next_birthday = datetime(next_birthday_year, birthday.month, birthday.day).date()
        
        #для проміжкової перевірки
        print(f"Next birthday for {user['name']}: {next_birthday}")
        
        if (next_birthday - today <= timedelta(days=30)) and (next_birthday - today >= timedelta(days=0)):
            if next_birthday.weekday() in [5, 6]:
                next_birthday += timedelta(days=(7 - next_birthday.weekday()))
        
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": next_birthday.strftime("%Y.%m.%d")
            })
            print(f"Added {user['name']}'s birthday to upcoming_birthdays.")
    
    return upcoming_birthdays


users = [
    {"name": "John", "birthday": "1990.05.12"},
    {"name": "Alice", "birthday": "1985.12.28"},
    {"name": "Bob", "birthday": "1995.03.02"}, # у боба день народження через 7 днів (меньше за 30) тому программа повинна привітати його
    {"name": "Emma", "birthday": "1992.11.15"}
]

upcoming_birthdays = (get_upcoming_birthdays(users))

for user in upcoming_birthdays:
    print(f"Happy birthday, {user['name']}! The celebration date is {user['congratulation_date']}")
