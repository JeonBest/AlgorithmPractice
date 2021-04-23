n, m = map(int, input().split())
j = int(input())

dist = 0
left = 1
dirt = -1 # -1 = right / 1 = left
for _ in range(j):
    right = int(input())
    newdirt = (left - right) // abs(left - right)

    if dirt < 0:
        dist += abs(left - right) - (m - 1)
        # (An-1 - An) * (An - An+1) < 0 이면, 이동거리 += |An - An+1| - (바구니수 - 1)
        # 바구니 이동해야할 방향이 바뀜
    elif dirt > 0:
        dist += abs(left - right)
        # (An-1 - An) * (An - An+1) > 0 이면, 이동거리 += |An - An+1|
        # 바구니 이동해야할 방향이 같음

    dirt = newdirt
    left = right
