def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fibonacci_number = fibonacci()
for i in range(100):
    print(next(fibonacci_number))
