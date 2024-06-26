# def fibonacci(n):
#     if n <= 1:
#         return n
#     elif n>1:
#         return (fibonacci(n-1) + fibonacci(n-2))

def fibonacci(n):
    if n < 1:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        a = 1
        b = 1
        for i in range(n-2):
            c = a + b
            a = b
            b = c
    return c
    
T = int(input())

# print(fibonacci(T))

for i in range(T):
    W = int(input())
    print(fibonacci(fibonacci(W)))