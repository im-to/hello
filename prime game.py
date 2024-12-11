import random

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_primes_in_range(start, end):
    prime_count = 0
    prime_numbers = []
    
    for num in range(start, end + 1):
        if is_prime(num):
            prime_numbers.append(num)
            prime_count += 1
    
    return prime_numbers, prime_count

start = random.randint(1,1000)
end = start + random.randint(10,100)
primes, count = count_primes_in_range(start, end)

user_input = int(input(f"범위 {start}부터 {end}까지 소수의 갯수는? "))

if user_input == count:
    print("정답입니다")
else:
    print(f"틀렸습니다. 소수의 개수: {count}")

print(f"범위 {start}부터 {end}까지 소수: {primes}")