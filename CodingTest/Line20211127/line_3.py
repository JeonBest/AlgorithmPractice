def solution(board, durability):
    answer = -1
    # right, down, left, up
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    # reflectionDirection[obstacle idx][source direction idx] = dest direction idx
    reflectDirection = [[2, 3, 1, 0], [1, 3, 0, 2], [2, 0, 3, 1], [3, 2, 0, 1], [2, 3, 0, 1]]
    isDistanceAdd = [[False, False, True, True], [True, False, False, True], [False, True, True, False], [True, True, False, False], [False, False, False, False]]
    
    x = 0
    y = -1
    dxyIdx = 0
    maxX = len(board) - 1
    maxY = len(board[0]) - 1
    
    while True:
        answer += 1
        
        nextX = x + dx[dxyIdx]
        nextY = y + dy[dxyIdx]
        
        if nextX < 0 or nextX > maxX or nextY < 0 or nextY > maxY:
            break
        
        x = nextX
        y = nextY
        
        if board[x][y] == 0:
            answer += 1
            continue
        
        
        
    
    return answer

def assertCode(answer, submit):
    print("\t", "----- PASS -----" if answer == submit else "----- FAIL -----",
          "\nExpect:", answer, "\tResult:", submit)

def main():
    pass

if __name__ == '__main__':
    main()