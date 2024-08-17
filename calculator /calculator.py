from data import greetings, choose, operations

print(greetings)

def two_number_request():
    num_a = input("Type first number: ")
    num_b = input("Type second number: ")

    try : 
        num_a = int(num_a)
        num_b = int(num_b)
    except: 
        return None, None, True
    
    return num_a, num_b, None


while True: 
    operation = input(choose).lower().replace(" ", "")

    if operation in ("e", "-1"): 
        exit()

    elif operation in operations: 
        a, b, err = two_number_request()

        if err:
            print("Error happened")
            continue
        
        if operation in ("1", "ad"):
            print(f'{a} + {b} = {a+b}')
        elif operation in ("2", "su"):
            print(f'{a} - {b} = {a-b}')
        elif operation in ("3", "mu"):
            print(f'{a} * {b} = {a*b}')
        elif operation in ("4", "di"):
            try: 
                c = a / b
            except:
                c = "Inf"
            print(f'{a}/{b} = {c}')
        
        print('\n\n')
    else:
        continue