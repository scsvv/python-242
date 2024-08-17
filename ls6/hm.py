N = input("Enter N:")
try:
    N = int(N)
    if N<1:
        raise ZeroDivisionError("Число должно быть больше или равно 1")
except ZeroDivisionError as err:
    print(err)
    exit()
except ValueError: 
    print("Incorrect Data")
    exit()


data = 0
for i in range(1, N+1):
    data += 1 / i
print(data)