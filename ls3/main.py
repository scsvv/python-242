# mock = 'qWerty'
# password = input("Enter your password: ")

# if password == mock:
#     print("Welcome!")
# else: 
#     print("Access dined")

# number = input("Type number: ")

# try: 
#     number = int(number)
# except:
#     print("Error 1: Not valid datatype")
#     exit()

# if number % 2 == 0:
#     print("Четное")
# else:
#     print("Не честное") 

# x = input("Type number: ")
# y = input("Type number: ")

# try: 
#     x = int(x)
#     y = int(y)
# except: 
#     exit()

# if (x > 0 and y > 0) and (x < 9 and y < 9):
#     if (x + y) % 2 == 0:
#         print("Black")
#     else: 
#         print("White")
# else: 
#     print("Out scope 8x8")

# x = input("Type x: ")
# y = input("Type y: ")

# try: 
#     x = int(x)
#     y = int(y)
# except: 
#     exit()

# if x > y:
#     print(x)
# else: 
#     print(y)

# print( x if x > y else y )

# hour = input("Enter hour: ")
# try: 
#     hour = int(hour)
# except:
#     hour = 99

# if hour < 0 or hour > 24:
#     print("Incorrect time")
# elif hour >= 22 or hour < 5:
#     print("Night")
# elif hour < 11:
#     print("Morning")
# elif hour < 17:
#     print("Day time")
# elif hour < 22:
#     print("Evening")
# else: 
#     print("Unnamed error")

day = input("type day's number: ")
days = ("Monday", "Tuesday", "Wendsday", "Thursday", "Friday", "Saturday", "Sunday")
try: 
    day = int(day)
except: 
    day = -999

try: 
    print(days[day-1])
except:
    print("Incorect data")



