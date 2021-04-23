# -*- coding: utf-8 -*-
import math
from itertools import permutations
import string

def is_prime_number(n):
    # 2부터 n까지의 모든 수에 대하여 소수 판별
    array = [True for i in range(n+1)] # 처음엔 모든 수가 소수(True)인 것으로 초기화(0과 1은 제외)

    # 에라토스테네스의 체
    for i in range(2, int(math.sqrt(n)) + 1): #2부터 n의 제곱근까지의 모든 수를 확인하며
        if array[i] == True: # i가 소수인 경우(남은 수인 경우)
            # i를 제외한 i의 모든 배수를 지우기
            j = 2
            while i * j <= n:
                array[i * j] = False
                j += 1

    return [False, False] + [ array[i] for i in range(2, n+1) ]

def solution(numbers):

    answer = 0
    isPrime = is_prime_number(10 ** len(numbers))

    candidate = []
    for i in range(1, len(numbers) + 1):
        candidate += map(int, map(''.join, map(list, (permutations(numbers, i)))))

    for num in set(candidate):
        if isPrime[num]:
            answer += 1    

    return answer

test = "011"
print(solution(test))