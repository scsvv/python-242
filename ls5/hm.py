from random import randint 

numbers = list()

for i in range(10):
    numbers.append(randint(0, 10))

print(numbers)

uniq_numbers = list()
first_max = -1
second_max = -1

for number in numbers:

    if number > first_max:
        second_max = first_max
        first_max = number
    elif number > second_max and number == first_max: 
        second_max = number

    if numbers.count(number) == 1:
        uniq_numbers.append(number)
    
print(first_max, second_max)
print(uniq_numbers)