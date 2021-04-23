# -*- coding: utf-8 -*-
import math

def yaksu(number):
    ret = []
    for i in range(1, int(math.sqrt(number)) + 1):
        if number % i == 0:
            ret.append((i, number/i))
    return ret

def solution(brown, yellow):
    answer = []

    for candidate in yaksu(brown + yellow):
        
        if (candidate[0]-2)*(candidate[1]-2) == yellow:
            return list([candidate[1], candidate[0]])

    return answer
