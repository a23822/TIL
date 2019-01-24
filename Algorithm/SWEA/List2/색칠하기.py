tc = int(input())

for t in range(tc):
    grid = [[0]*10 for i in range(10)]   # [[0]*10]* 10 하면 나중에 같은 값 10개로 나옴. 주의!!
    N = int(input())
    color = []
    for n in range(N):
        temp = list(map(int, input().split()))
        color.append(temp)
    for c in color:
        for i in range(c[0], c[2]+1):
            for j in range(c[1], c[3]+1):
                if grid[i][j] == 0:
                    grid[i][j] = [c[4]]
                elif not c[4] in grid[i][j]:
                    grid[i][j].append(c[4])

    print(grid)
    cnt = 0
    for i in range(10):
        for j in range(10):
            if grid[i][j] != 0 and len(grid[i][j])>1:
                cnt += 1
    
    print('#{} {}'.format(t+1 , cnt))