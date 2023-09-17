def is_1(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate(N):
    count = 0
    number = 2
    while count < N:
        if is_1(number):
            yield number
            count += 1
        number += 1


N = 10  
for i in generate(N):
    print(i)