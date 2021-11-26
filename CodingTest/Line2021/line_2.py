def solution(inputArray):
    answer = [-1] * len(inputArray)
    monotoneStack = []
    
    # left to right
    for idx, inputNum in enumerate(inputArray):
        
        while len(monotoneStack) > 0 and monotoneStack[-1][1] <= inputNum:
            monotoneStack.pop()

        if len(monotoneStack) > 0:
            answer[idx] = monotoneStack[-1][0]
            
        monotoneStack.append((idx, inputNum))
    
    monotoneStack.clear()
    # right to left
    for reversedIdx, inputNum in enumerate(inputArray[::-1]):
        idx = len(inputArray) - reversedIdx - 1
        
        while len(monotoneStack) > 0 and monotoneStack[-1][1] <= inputNum:
            monotoneStack.pop()

        if len(monotoneStack) > 0:
            if answer[idx] == -1 or idx - answer[idx] > monotoneStack[-1][0] - idx:
                answer[idx] = monotoneStack[-1][0]
            
        monotoneStack.append((idx, inputNum))
    
    return answer
    
def assertCode(answer, submit):
    print("\t", "----- PASS -----" if answer == submit else "----- FAIL -----",
          "\nExpect:", answer, "\tResult:", submit)

def main():
    assertCode([1,-1,1,2,2] ,solution([3,5,4,1,2]))
    assertCode([1,2,10,2,3,6,3,6,9,10,-1,10], solution([5,19,46,20,10,16,18,15,15,29,47,20]))

if __name__ == '__main__':
    main()
    