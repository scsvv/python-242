# # ? 
# week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# print(week[0])
# print(week[-1])

# month = []


from random import randint

numbers = []
for i in range(10):
    numbers.append(randint(0, 10))

# print(numbers)

# numbers.append("E")
# print(numbers)

# numbers.insert(100, "A")
# print(numbers)
# # length 
# print(len(numbers))

# numbers.pop()
# print(numbers)

# numbers.remove("E")
# print(numbers)


# a = [1, 3, 4, 5]
# b = [4, 5, 6, 7]
# c = []

# for number in b: 
#     if a.count(number) == 0:
#         c.append(number)

# print(c)

print(numbers)

max_value = numbers[0]
for number in numbers: 
    if number > max_value:
        max_value = number

print(max_value)

print(max(numbers))