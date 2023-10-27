
import sys

def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        n = int(sys.argv[1])
        print(fib(n))