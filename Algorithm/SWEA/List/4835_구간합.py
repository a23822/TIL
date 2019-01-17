T = int(input()) # 테스트케이스

for n in range(T):
    nm = list(map(int, input().split())) # N 개의 정수 M개의 합이 가장 큰 경우/작은 경우
    a = list(map(int, input().split())) # 정수 리스트

    res = []
    for i in range(nm[0]-nm[1]+1):
        sum = 0
        for j in range(nm[1]):
            sum+=a[i+j]
        res.append(sum)
    print(f'#{n+1} {max(res)-min(res)}')