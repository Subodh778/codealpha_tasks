def fibonacci_generator():
    a, b = 0, 1
    while True:
        a , b = b, a+b
        yield b
        


inp = int(input("Enter the number you want to generate fibonacci series upto: "))

fib_gen = fibonacci_generator()
for i in range(inp):
    print(next(fib_gen))