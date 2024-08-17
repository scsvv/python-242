# K = input("Enter K: ")
# N = input("Enter N: ")

# try:
#     N = int(N)
#     K = int(K)
# except:
#     print("Invalid Data Type")

# if K < N: 
#     for i in range(K, N+1): print(i)
# elif N < K:
#     for i in range(K, N-1, -1): print(i)
# else:
#     print(N)

N = input("Enter N: ")

try:
    N = int(N)
    if N < 1:
        raise ZeroDivisionError
except:
    print("Incorrect Data")
    exit()

data = 0
for i in range(0, N):
    data += 1 + N/10

print(data)
