tc = int(input())

for t in range(tc):
    c = input()
    txt = input()
    cnt = 0
    for cp in c:
        cnt2 = 0
        for tp in txt:
            if cp == tp:
                cnt2 += 1
        
        if cnt2 > cnt:
            cnt = cnt2
    
    print("#{} {}".format(t+1, cnt))