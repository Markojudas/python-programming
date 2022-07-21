from time import time

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    return fib(n - 1) + fib (n - 2)

n = 10

start = time()
print("The fibonacci number of", n, "is:", fib(n))
end = time()

print("elapsed time: ", (end-start))