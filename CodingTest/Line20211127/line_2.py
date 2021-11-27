def solution(r, c):
    answer = [[0]*c for _ in range(r)]
    # dxyIdx가 3이거나 7일때는 한번만 이동
    dx = [0, 1, 0, -1, 0, -1, 0, 1]
    dy = [-1, 0, 1 ,0, -1, 0, 1, 0]

    x = 0
    y = c-1
    dxyIdx = 0
    cnt = 1
    while True:
        # 방문 안한 격자일 경우
        if answer[x][y] == 0:
            answer[x][y] = cnt
            cnt += 1
        
        # 방향 설정
        isEnd = True
        for _ in range(0, 8):
            nextX = x + dx[dxyIdx]
            nextY = y + dy[dxyIdx]
            if nextX >= 0 and nextX < r and nextY >= 0 and nextY < c and answer[nextX][nextY] == 0:
                # print("dxyIdx:", dxyIdx)
                # print("nextX:", nextX, "nextY:", nextY)
                isEnd = False
                x = nextX
                y = nextY
                if dxyIdx == 3 or dxyIdx == 7:
                    dxyIdx = (dxyIdx + 1) % 8
                break
            else:
                dxyIdx = (dxyIdx + 1) % 8
        
        if isEnd:
            break
    
    return answer

def assertCode(answer, submit):
    print("\t", "----- PASS -----" if answer == submit else "----- FAIL -----",
          "\nExpect:", answer, "\tResult:", submit)

def main():
    print(solution(5, 4))
    print(solution(3, 5))

if __name__ == '__main__':
    main()
    