tc = int(input())

for t in range(tc):
    N = int(input())
    num_list = list(map(int, input().split()))
    nums = sorted(num_list)
    print(nums)
    ans = []
    big = []
    small = []
    for n in range(N):
        if n >= int(N/2):
            big.append(nums[n])
        else:
            small.append(nums[n])
    p = 0
    if len(big) != len(small):
        p = big.pop(0)
    big.sort(reverse=True)

    for i in range(int(N/2)):
        ans.append(big[i])
        ans.append(small[i])

    if p != 0:
        ans.append(p)

    
    if N >= 10:
        print('#{} '.format(t+1), end="")
        for i in range(10):
            if i != 9:
                print('{}'.format(ans[i]), end=" ")
            else:
                print('{}'.format(ans[i]))
    else:
        print('#{} '.format(t+1), end="")
        for i in range(N):
            if i != N-1:
                print('{}'.format(ans[i]), end=" ")
            else:
                print('{}'.format(ans[i]))