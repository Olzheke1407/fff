def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


n = int(input('Введите сколько чисел фибоначчи хотите сгенерировать: '))  
gen = fibonacci()
numbers = [next(gen) for _ in range(n)]

print(numbers)