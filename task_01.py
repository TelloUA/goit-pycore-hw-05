def caching_fibonacci():
    cache = {}

    def fibonacci(n):
        # check basic numbers
        if n <= 0: return 0
        if n == 1: return 1

        # check dictionary
        value = cache.get(n)
        if value: return value

        # fill dictionary
        cache[n] = fibonacci(n - 1) + fibonacci (n - 2)
        return cache[n]
    
    # return function
    return fibonacci

# get function fibonacci
fib = caching_fibonacci()

# use function
print('result', fib(10))  # Виведе 55
