from random import randint

def amount_list(numbers_list):
    numbers_sum = 0

    for number in numbers_list:
        numbers_sum += number
    
    return numbers_sum

def list_generator(N, min = -100, max = 1000):
    generated_list = list()
    for i in range(N):
        generated_list.append(randint(min, max))
    
    return generated_list

a = list_generator(10)
b = list_generator(10)
c = list_generator(10)

print(f'{a}\n{b}\n{c}\n')

print(amount_list(a))
print(amount_list(b))
print(amount_list(c))