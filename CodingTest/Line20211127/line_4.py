def solution(grid):
    answer = 0
    # x, y의 visit정보는 visit[x*10000 + y]에 저장
    X_IDX_NUM = 10000
    visit = [False]*X_IDX_NUM*1000
    newVisit = [False]*X_IDX_NUM*1000
    
    maxX = len(grid) - 1
    maxY = len(grid[0]) - 1
    
    dx = [0, 0, 1, -1]
    dy = [-1, 1, 0, 0]
    
    for xIdx, x in enumerate(grid):
        for yIdx, y in enumerate(x):
            if grid[xIdx][yIdx] == 0:
                visit[xIdx*X_IDX_NUM+yIdx] = True

    isFinish = False
    while True:
        isFinish = True
        # print(answer)
        # print(grid)
        for xIdx, x in enumerate(grid):
            for yIdx, y in enumerate(x):
                
                if visit[xIdx*X_IDX_NUM + yIdx]:
                    continue
                
                isVisitAround = False
                
                for dxyIdx in range(0, 4):
                    nextX = xIdx + dx[dxyIdx]
                    nextY = yIdx + dy[dxyIdx]
                    
                    if not nextX >= 0 and nextX <= maxX and nextY >= 0 and nextY <= maxY:
                        continue
                    
                    if visit[nextX*X_IDX_NUM + nextY] == True:
                        newVisit[xIdx*X_IDX_NUM + yIdx] = True
                        isVisitAround = True
                        
                if isVisitAround:
                    grid[xIdx][yIdx] = answer+1
                    isFinish = False
                    
        for idx, newVisitElement in enumerate(newVisit):
            if newVisitElement:
                visit[idx] = True

        if isFinish:
            break
        answer += 1
        
    # print(grid)
    return answer

def assertCode(answer, submit):
    print("\t", "----- PASS -----" if answer == submit else "----- FAIL -----",
          "\nExpect:", answer, "\tResult:", submit)

def main():
    assertCode(3, solution([[0, 0, 1, 1, 1], [1, 0, 0, 1, 1], [0, 0, 0, 0, 1], [1, 1, 1, 1, 1], [0, 0, 1, 0, 1]]))

if __name__ == '__main__':
    main()