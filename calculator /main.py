print("""
   _____      _            _       _             
  / ____|    | |          | |     | |            
 | |     __ _| | ___ _   _| | __ _| |_ ___  _ __ 
 | |    / _` | |/ __| | | | |/ _` | __/ _ \| '__|
 | |___| (_| | | (__| |_| | | (_| | || (_) | |   
  \_____\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   

Custom Calculator v0.0.1 alpha 

Hello User, 
This program is first version of calculator. 

Please, follow indtuction below. \n\n
""")

number1 = input("Please, type number1: ")
number2 = input("\nPlease, type number2: ")

try: 
    number1 = int(number1)
    number2 = int(number2)
except:
    print("Error 1: Not valid data type")
    exit()

print(f"Result: {number1 + number2}")

operation = input("""
Please select operation from the list: 

1. +
2. -
3. *
4. /
5. ** 

Others: Exit
""")

try: 
    operation = int(operation)
except:
    exit()