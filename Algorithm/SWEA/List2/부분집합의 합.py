tc = int(input())
A = []
for i in range(12):
    A.append(i+1)

for t in range(tc):
    a = list(map(int, input().split()))
    cnt = 0
    for i in range(1<<len(A)):
        sum = 0
        temp = []
        for j in range(len(A)+1):
            if i & (1<<j):
                sum += A[j]
                temp.append(A[j])
        if sum == a[1] and len(temp) == a[0]:
            print(temp)
            cnt += 1
    
    print('#{} {}'.format(t+1, cnt))