for t in range(10):
    tc = int(input())
    arr = []
    for i in range(100):
        arr.append(list(map(int, input().split())))
 
    ans = 0
    sum_diag1 = 0
    sum_diag2 = 0
    for i in range(100):
        sum = 0
        for j in range(100):
            sum += arr[i][j]
        if ans < sum:
            ans = sum
        sum = 0
        for j in range(100):
            sum += arr[j][i]
        if ans < sum:
            ans = sum
 
        sum_diag1 += arr[i][i]
        sum_diag2 += arr[99-i][i]
    if ans < sum_diag1:
        ans = sum_diag1
    if ans < sum_diag2:
        ans = sum_diag2
 
    print('#{} {}'.format(tc, ans))