def solution(numbers, target):
    answer = 0

    if len(numbers) == 1:
        if numbers[0] == target:
            answer += 1
        if numbers[0] == -target:
            answer += 1

    else:
        answer += solution(numbers[1:], target - numbers[0]) + solution(numbers[1:], target + numbers[0])

    return answer

testcase = [[1,1,1,1,1], 3]
print(solution(testcase[0], testcase[1]))