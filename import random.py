import random


target_number = random.randint(1, 100)
attempts = 0

while True:
    try:
        user_input = input("숫자를 입력하세요: ")
        guess = int(user_input)

        if guess < 1 or guess > 100:
            print("1부터 100 사이의 숫자를 입력해주세요.")
            continue

        attempts += 1

        if guess < target_number:
            print("UP")
        elif guess > target_number:
            print("DOWN")
        else:
            print(f"YOU WIN! attempt:{attempts}")
            break

    except ValueError:
        print("유효한 숫자를 입력해주세요.")