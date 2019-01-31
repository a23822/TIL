tc = int(input())

for t in range(tc):
    a = list(map(int, input().split())) # 첫번째껀 N, 두번재껀 M
    str_list = [0 for _ in range(2 * a[0])]
    lth = a[0] * (a[0]-a[1]+1)
    for i in range(a[0]):
        str_list[i] = input()
    

    for j in range(a[0]):
        temp = ""
        for k in range(a[0]):
            temp += str_list[k][j]
        str_list[a[0]+j] = temp
    
    for txt in str_list:
        for idx in range(0, a[0]-a[1]+1):
            if txt[idx:idx+a[1]+1] == txt[idx:idx+a[1]+1][::-1]:
                print("#{} {}".format(t+1, txt[idx:idx+a[1]+1]))
                break