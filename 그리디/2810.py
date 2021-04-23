n = int(input()) # 문자열 길이
chairs = list(input()) # 좌석 형태

cnt = 0
for c in chairs:
    if c == 'L':
        cnt += 1

cnt //= 2 # cnt는 LL의 등장횟수

# 예외처리
if cnt == 0:
    print(n)
else:
    print(n + 1 - cnt)
