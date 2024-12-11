import random


number = random.randint(1,10)
operator = 1
result = 0

for x in range(1,5):
    print(f"print{number}/{operator}")
    if operator == 1:
        result += number
    elif operator == 2:
        result += number
    elif operator == 3:
        result *= number
    else:
        result /= number

    number = random.randint(1,100)
    operator = random.randint(1,4)

print(result)