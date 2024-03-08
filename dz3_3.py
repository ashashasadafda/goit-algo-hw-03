# #завдання 3 (виправив)
import re

def normalize_phone(phone_number):
    
    normalized_number = re.sub(r'\D', '', phone_number)
    
    # if normalized_number.startswith("38"):
    #     print("я починаюсь з 38") #dlya perevirku       64 строка: normalized_number = re.sub(r'\D', '', phone_number) видаляє плюсик на початку кожного номера, тому і не працювало :)
    #     return normalized_number
    
    if normalized_number.startswith("38"):
        print("я починаюсь з 38, тому я додам тільки '+': ") #dlya perevirku
        return '+' + normalized_number + '\n'
    
    elif normalized_number.startswith("0"):
        print("я починаюсь з 0, тому я додам '+38': ") #dlya perevirku
        return '+38' + normalized_number[1:] + '\n'
    
    else:
        return '+380' + normalized_number[3:] + '\n' # додав зрізи
        

phone_numbers = [
    "+38(050)123-32-34",
    "0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
    "+380 68 483 82 93", #dlya perevirku
    "432 11 222 22 22"
]

for phone_number in phone_numbers:
    print(normalize_phone(phone_number))
    
   