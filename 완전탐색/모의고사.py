# -*- coding: utf-8 -*-
def solution(answers):
    answer = []

    n = len(answers)

    supo1 = [1, 2, 3, 4, 5]
    lensupo1 = len(supo1)
    supo2 = [2, 1, 2, 3, 2, 4, 2, 5]
    lensupo2 = len(supo2)
    supo3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    lensupo3 = len(supo3)

    cnt = [0, 0, 0]
    for idx, ans in enumerate(answers):
        if ans == supo1[idx % lensupo1]:
            cnt[0] += 1
        if ans == supo2[idx % lensupo2]:
            cnt[1] += 1
        if ans == supo3[idx % lensupo3]:
            cnt[2] += 1
    
    cntMax = max(cnt)
    for idx, c in enumerate(cnt):
        if cntMax == c:
            answer.append(idx+1)

    return answer