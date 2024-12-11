def is_prime(n):
    """소수인지 확인하는 함수"""
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_primes_in_range(start, end):
    """주어진 범위에서 소수의 개수를 세는 함수"""
    prime_count = 0
    prime_numbers = []  # 소수를 저장할 리스트
    
    for num in range(start, end + 1):
        if is_prime(num):
            prime_numbers.append(num)
            prime_count += 1
    
    return prime_numbers, prime_count


start = 10
end = 67
primes, count = count_primes_in_range(start, end)

user_input = int(input(f"범위 {start}부터 {end}까지 소수의 갯수는? "))

if user_input == count:
    print("정답입니다")
else:
    print(f"틀렸습니다. 소수의 개수: {count}")

print(f"범위 {start}부터 {end}까지 소수: {primes}")