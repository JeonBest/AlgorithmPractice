from collections import deque

def solution(priorities, location):
    answer = 0
    
    deq = deque()
    
    deq.extend(enumerate(priorities))
    maxPriority = findMaxElement(deq)
    
    while len(deq) > 0:
        frontElement = deq.popleft()
        if frontElement[1] < maxPriority:
            deq.append(frontElement)
        else:
            # 인쇄
            print(frontElement)
            answer += 1
            maxPriority = findMaxElement(deq)
            if frontElement[0] == location:
                break
    
    return answer

def findMaxElement(deq):
    maxElement = 0
    for element in deq:
        if element[1] > maxElement:
            maxElement = element[1]
    return maxElement

def main():
    print(solution([2,1,3,2], 2))
    print(solution([1,1,9,1,1,1], 0))

if __name__ == '__main__':
    main()
    
