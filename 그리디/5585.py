n = 1000 - int(input())

coins = [500, 100, 50, 10, 5, 1]

ans = 0 # 거스름동전 갯수

for c in coins:
    ans += n // c
    n = n % c

print(ans)