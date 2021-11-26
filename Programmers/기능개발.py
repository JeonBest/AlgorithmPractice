import math

def solution(progresses, speeds):
    answer = []
    
    workDays = []
    for idx, progress in enumerate(progresses):
        workDay = math.ceil((100 - progress) / speeds[idx])
        workDays.append(workDay)
    
    # print(workDays)

    cnt = 1
    localMax = workDays[0]
    for idx in range(1, len(workDays)):
        if (workDays[idx] > localMax):
            localMax = workDays[idx]
            answer.append(cnt)
            cnt = 0
        cnt += 1
        # print("workDays:",workDays[idx],"\tcnt:", cnt, "\tlocalMax:", localMax)
    if (cnt > 0):
        answer.append(cnt)

    return answer

def main():
    print(solution([93,30,55], [1,30,5]))
    print(solution([95,90,99,99,80,99], [1,1,1,1,1,1]))
    print(solution([99,99,99,99,99], [1,1,1,1,1]))

if __name__ == '__main__':
    main()