

# fibonati - x = soma dos dois anteriores
# caso geral = fib(n) = fib[n-1] + fib[n-2]
# caso base = fib(0) = 0
#fib(i) = 1

num = []
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib(n-1) + fib(n-2)

print("fibo",fib(10))

