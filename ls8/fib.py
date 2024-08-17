def memoize(func):
    cache = {}

    def wrapper(*args):
        if args in cache:
            return cache[args]
        else:
            cache[args] = func(*args)
            return cache[args]
    return wrapper

@memoize
def fib(N):
    if N == 1 or N == 2:
        return 1 
    
    return fib(N - 1) + fib(N - 2)

print(fib(3), fib(10), fib(56))
