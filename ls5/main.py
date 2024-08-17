# from random import randint

# numbers = list()
# for i in range(10):
#     numbers.append(randint(0, 10))

# # print(numbers)
# # print(numbers[:5])
# # print(numbers[5:])

# # print(numbers[::-1])
# # sum_of_numbers = 0
# # for i in range(2, 101, 2):
# #     sum_of_numbers += i

# # print(sum_of_numbers)

# i = 0 
# while i <=10: 
#     print(i)
#     i += 1

mock_password = 'asd'
correct_password = False
i = 3
# for i in range(3):
#     password = input("Enter password: ")

#     if mock_password == password:
#         print("Correct")
#         break
#     else: 
#         print("Incorrect")

while not correct_password and i > 0:
     password = input("Enter password: ")
     if mock_password == password:
        print("Correct")
        correct_password = True
     else: 
        i -= 1
        print("Incorrect")
