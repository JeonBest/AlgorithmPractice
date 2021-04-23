N = int(input())

# N보다 작은 가장 큰 5의 배수
M = N - (N % 5)
# 5kg짜리 봉지 수
cnt5 = M // 5

# N - M이 3의 배수일 때까지 반복
while (N - M) % 3 != 0:

    # M보다 작은 가장 큰 5의 배수
    M -= 5
    cnt5 -= 1

    # 정확하게 N킬로그램을 만들 수 없는 경우
    if M < 0:
        print(-1)
        exit(0)

print(cnt5 + (N - M) // 3)