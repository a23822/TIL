for n in range(10):
    index = int(input())
    bd_list = [int(i) for i in input().split()]
    # list(map(int,input().split()))
    res = 0
    for i in range(2, index-2): #for 대신 while로
        temp = [int(bd_list[i])-int(bd_list[i-2]), int(bd_list[i])-int(bd_list[i-1]), int(bd_list[i])-int(bd_list[i+1]), int(bd_list[i])-int(bd_list[i+2])]
        if min(temp) < 0:
            continue
        else:
            res += min(temp)
    # 다른 풀이론 bd_list[i] 가 가장 높을때를 구해서
    # 가장 높을 경우 조망권을 구해서 res를 더함.
    """
    N = int(input())
    heights = list(map(int, input.split()))
    view = 0

    for i in range(2, N-2):
        side = getMax(i)
        if side < heights[i]:
            view += heights[i] - side

    print("#%d %d" % (tc.view))


    """
    print(f"#{n+1} {res}")