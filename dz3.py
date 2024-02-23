#завдання 1, 4
from datetime import datetime as dt
from datetime import datetime, timedelta
#завдання 2
import random
#завдання 3
import re



# #завдання 1 (виправив)
# def get_days_from_today(date):
    
#     try:
#         inputDate = dt.strptime(date, '%Y-%m-%d')
#         currentDate = dt.now()
#         delta = currentDate - inputDate
        
#         return delta.days

#     except:
#         return ValueError

# print(get_days_from_today('2007-09-17'))



# # #завдання 2 (виправив)
def get_numbers_ticket(min, max, quantity):
    myList = []
    if(min < max):
        while len(myList) < quantity:
            xd = random.randint(min, max)
            if xd not in myList:
                myList.append(xd)
                
        myList.sort()
        return myList
    else: 
        min, max = max, min # свапаємо значення місцями
        while len(myList) < quantity:
            xd = random.randint(min, max)
            if xd not in myList:
                myList.append(xd)
        
        myList.sort()
        return myList
                
                
def guess_ticket(ticket_num, ticket_len) -> int:
    ticket_len = len(ticket_num)
    guessedNums = 0
    
    for x in range(ticket_len):
        xd = int(input("enter num: "))
        if xd == ticket_num[x]:
            guessedNums += 1
            print(f"u guessed {x+1} num! lets go to the next -> ")
        else:
            print("unluck :(")
    
    return guessedNums
    
      
    
list1 = get_numbers_ticket(15, 5, 5)
print(list1) # щоб перевіряти

print(f"\nu guessed {guess_ticket(list1, 6)} nums!!! congrats =)")



# #завдання 3 (виправив)
# def normalize_phone(phone_number):
    
#     normalized_number = re.sub(r'\D', '', phone_number)
    
#     # if normalized_number.startswith("38"):
#     #     print("я починаюсь з 38") #dlya perevirku       64 строка: normalized_number = re.sub(r'\D', '', phone_number) видаляє плюсик на початку кожного номера, тому і не працювало :)
#     #     return normalized_number
    
#     if normalized_number.startswith("38"):
#         print("я починаюсь з 38, тому я додам тільки '+': ") #dlya perevirku
#         return '+' + normalized_number + '\n'
    
#     else:
#         print("я не починаюсь ні на 38, ні на +38, тому я додам '+38': ") #dlya perevirku
#         return '+38' + normalized_number + '\n'
        

# phone_numbers = [
#     "+38(050)123-32-34",
#     "0503451234",
#     "(050)8889900",
#     "38050-111-22-22",
#     "38050 111 22 11   ",
#     "+380684838293" #dlya perevirku
# ]

# for phone_number in phone_numbers:
#     print(normalize_phone(phone_number))
    
    
    
#завдання 4 (хоч вбийте не можу зрозуміти чого повертає пустий список =(. )
# def get_upcoming_birthdays(users) -> list:
#     today = datetime.today().date()
    
#     upcoming_birthdays = []
    
#     for user in users:
#         birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        
#         next_birthday_year = today.year
        
#         if birthday < today:
#             next_birthday_year += 1
        
#         next_birthday = datetime(next_birthday_year, birthday.month, birthday.day).date()
        
#         #для проміжкової перевірки
#         print(f"Next birthday for {user['name']}: {next_birthday}")
        
#         if (next_birthday - today <= timedelta(days=365)) and (next_birthday - today >= timedelta(days=0)):
#             if next_birthday.weekday() in [5, 6]:
#                 next_birthday += timedelta(days=(7 - next_birthday.weekday()))
        
#             upcoming_birthdays.append({
#                 "name": user["name"],
#                 "congratulation_date": next_birthday.strftime("%Y.%m.%d")
#             })
#             print(f"Added {user['name']}'s birthday to upcoming_birthdays.")
    
#     return upcoming_birthdays


# users = [
#     {"name": "John", "birthday": "1990.05.12"},
#     {"name": "Alice", "birthday": "1985.12.28"},
#     {"name": "Bob", "birthday": "1995.08.02"},
#     {"name": "Emma", "birthday": "1992.11.15"}
# ]

# print(get_upcoming_birthdays(users))

# for user in upcoming_birthdays:
#     print(f"Happy birthday, {user['name']}! The celebration date is {user['congratulation_date']}")
