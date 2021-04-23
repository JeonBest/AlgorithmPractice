# -*- coding: utf-8 -*-
import copy

def solution(tickets):
    sortedTickets = copy.deepcopy(tickets)
    sortedTickets.sort()
    answer = []

    startTicketsIdx = []
    for idx, ticket in enumerate(sortedTickets):
        if ticket[0] == "ICN":
            startTicketsIdx.append(idx)

    for startTicketIdx in startTicketsIdx:
        
        dfs = [startTicketIdx]
        visit = [0] * len(sortedTickets)
        visit[startTicketIdx] = 1

        while dfs:
            curTicketIdx = dfs[-1]
            flag = 0

            for nextTicketIdx, nextTicket in enumerate(sortedTickets):
                # 현재 티켓의 도착지와 다음 티켓의 출발지가 같아야 연결가능함
                if nextTicket[0] == sortedTickets[curTicketIdx][1] and not visit[nextTicketIdx]:
                    dfs.append(nextTicketIdx)
                    visit[nextTicketIdx] = 1
                    flag = 1
                    break
            
            # dfs에서 stack빠져나갈 때
            if not flag:
                answer.append(sortedTickets[dfs.pop()][1])

        # 모든 티켓을 사용했는지 검사
        if 0 in visit:
            answer = []
        else:
            answer.append("ICN")
            answer.reverse()
            return answer

    return answer

test = [["ICN", "A"], ["ICN", "A"], ["A", "ICN"], ["A", "C"]]
print(solution(test))
