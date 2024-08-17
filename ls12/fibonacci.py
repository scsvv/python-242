

# N = 10000

# a, b, i = 0, 1, 1
# while True:
#     if i == N:
#         break
#     a, b = b, a+b
#     i += 1

# print(b)

def memo(func):
    cache = {}
    def wrapper(*args, **kwargs):
        if not args[0] in cache:
            cache[args[0]] = func(*args, **kwargs)
        
        return cache[args[0]]
    return wrapper


@memo
def fib(N):
    if N == 1 or N == 2:
        return 1
    else: 
        return fib(N-1) + fib(N-2)

print(fib(43))