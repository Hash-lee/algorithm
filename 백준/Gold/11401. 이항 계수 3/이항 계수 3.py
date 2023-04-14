import sys
# 페르마의 소정리
# p가 소수라는 가정 하에,
# n**p ≡ n (mod p)
# 이를 정리하면, n**(p-1) ≡ 1 (mod p)
# n * n**(p-2) ≡ 1 (mod p)
# n에 n**(p-2)를 곱한 나머지는 반드시 1이 된다.

MOD = 1000000007
N, K = map(int, sys.stdin.readline().split())
if N == K or K == 0:
    print(1)
    exit()

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result = (result * i) % MOD
    return result

def power(x, p):
    result = 1
    while 0 < p:
        if p % 2:
            result = (result * x) % MOD
        x = (x**2) % MOD
        p //= 2
    return result

answer = (factorial(N) * power(factorial(K)*factorial(N - K), MOD-2)) % MOD
print(answer)