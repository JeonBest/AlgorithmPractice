from collections import deque

def solution(n, computers):
    answer = 0

    visit = [0] * n

    bfs = deque([])

    for idx, isvisit in enumerate(visit):
        if isvisit:
            continue
        else:
            bfs.appendleft(idx)
            visit[idx] = 1
            answer += 1
        while bfs:
            _cur = bfs.pop()
            for _next, _isnext in enumerate(computers[_cur]):
                if _isnext and not visit[_next]:
                    bfs.appendleft(_next)
                    visit[_next] = 1

    return answer

com = [[1,1,0],[1,1,1],[0,1,1]]

print(solution(3, com))