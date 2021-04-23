from collections import deque

def solution(begin, target, words):
    answer = 0

    n = len(begin)
    visit = [0] * len(words)

    bfs = deque([(begin, 0)])
    
    while bfs:
        _now = bfs.pop()
        #print(_now[0])
        if _now[0] == target:
            return _now[1]
        
        for _idx, _next in enumerate(words):
            if visit[_idx]:
                continue
            
            numDiffAlpha = 0
            for letter_idx, letter in enumerate(_now[0]):
                if letter != _next[letter_idx]:
                    numDiffAlpha += 1
            if numDiffAlpha == 1:
                bfs.appendleft((_next, _now[1]+1))
                visit[_idx] = 1

    return answer

test1 = ["hot", "dot", "dog", "lot", "log", "cog"]
print(solution("hit", "cog", test1))