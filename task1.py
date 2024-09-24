import random

random_num = [random.randint(0, 10000) for i in range(10000)]

with open('text.txt', 'w') as file:
    for num in random_num:
        file.write(str(f'{num},'))

with open('text.txt', 'r') as file:
    for i in file:
        numbers = i.split(',')
        converted_num = [int(num) for num in numbers if num.isdigit()]
        print(sum(converted_num))
