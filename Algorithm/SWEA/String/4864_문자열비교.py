tc = int(input())

def BF(p, t):
    i = 0
    j = 0
    m = len(p)
    n = len(t)
    while j < m and i < n:
        if t[i] != p[j]:
            i = i-j
            j = -1
        i += 1
        j += 1
    if j == m:
        return 1
    else:
        return 0


for test in range(tc):
    str_list = ["" for _ in range(2)]
    for i in range(2):
        str_list[i] = input()
    
    p = str_list[0]
    t = str_list[1]
    answer = BF(p, t)

    print("#{} {}".format(test+1, answer))