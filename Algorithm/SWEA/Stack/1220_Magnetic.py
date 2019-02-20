for tc in range(10):
    side = int(input())
    board = []
    for _ in range(100):
        board.append(list(map(int,input().split())))

    cnt = 0

    for x in range(side):
        y = 0
        flag = False
        while y < side:
            if board[y][x] == 1:
                flag = True
            elif board[y][x] == 2 and flag:
                flag = False
                cnt += 1
            y += 1
    print('#{} {}'.format(tc+1, cnt))
