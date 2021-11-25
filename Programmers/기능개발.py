import math

def solution(progresses, speeds):
    answer = []
    
    workDays = []
    for idx, progress in enumerate(progresses):
        workDay = math.ceil((100 - progress) / speeds[idx])
        workDays.append(workDay)
    workDays.append(1000000)

    # print(workDays)

    cnt = 0
    for idx in range(0, len(workDays)-1):
        cnt += 1
        if (workDays[idx] < workDays[idx+1]):
            answer.append(cnt)
            cnt = 0
        # print(workDays[idx], cnt)

    return answer

def main():
    print(solution([93,30,55], [1,30,5]))
    print(solution([95,90,99,99,80,99], [1,1,1,1,1,1]))
    print(solution([99,99,99,99,99],[1,1,1,1,1]))

if __name__ == '__main__':
    main()