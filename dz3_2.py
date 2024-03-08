# #завдання 2 (виправив)
import random

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













# import random

# def sum_profit(text:str, func:callable):
#     return sum(func(text))
    
# def generator_numbers(text:str):
#     new_text = text.split(" ")
#     for word in new_text:
#         try:
#             number = float(word)
#             yield number
#         except ValueError:
#             pass
   
# text = """Загальний дохід працівника складається з декількох 
# # частин: 1000.01 як основний дохід, доповнений додатковими 
# # надходженнями 27.45 і 324.00 доларів."""         

# total_income = sum_profit(text, generator_numbers)
# print(f"Загальний дохід: {total_income}")



