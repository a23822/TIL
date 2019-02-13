def chk(f, p):
    if p == 99:
        if f[p-1] == 1:
            return -1
        else:
            return 0
    elif p == 0:
        if f[p+1] == 1:
            return 1
        else:
            return 0
    else:
        if f[p+1] == 1:
            return 1
        elif f[p-1] == 1:
            return -1
        elif f[p+1] == 0 and f[p-1] ==0:
            return 0
        


for _ in range(10):
    tc = int(input())
    board = [[] for _ in range(100)]
    for i in range(100):
        temp = list(map(int, input().split()))
        board[99-i] = temp
    point = 0

    for i in range(100):
        if board[0][i] == 2:
            point = i
            break

    cnt = 1
    while cnt < 100:
        floor = board[cnt-1]
        print(floor[point])    
        if chk(floor, point) == 1:
            while True:
                if point == 99:
                    break
                elif point != 99 and floor[point+1] == 0:
                    break
                else:
                    point += 1
        elif chk(floor, point) == -1:
            while True:
                if point == 0:
                    break
                elif point != 0 and floor[point-1] == 0:
                    break
                else:
                    point -= 1

        cnt += 1
    print('#{} {}'.format(tc, point))