T = int(input()) # 테스트케이스

for n in range(T):
    N = int(input()) #카드 장수
    a = list(map(int, input())) #카드 리스트

    list = []
    for j in a:
        if not j in list:
            list.append(j)
    res = []
    for k in list:
        cnt = 0
        for j in a:
            if k == j:
                cnt += 1

        res.append(cnt)

    cnt2 = 0
    for q in res:
        if q == max(res):
            cnt2+=1

    www = []
    if cnt2 > 1:
        for k in list:
            if res[list.index(k)] == max(res):
                www.append(k)
    else:
        www.append(max(list))

    print(f'#{n+1} {max(www)} {res[www.index(max(www))]}')

"""

T = int(input()) # 테스트케이스

for n in range(T):
    N = int(input()) #카드 장수
    a = list(map(int, input())) #카드 리스트
    dic = {}
    for i in a:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1


    res2 = max(dic.values())
    res = []
    sorted_dic = sorted(dic.items(), key=lambda x: x[1] , reverse=True)
    for j in sorted_dic:
        if j[1] == res2:
            res.append(j[0])
    print(f'#{n+1} {max(res)} {res2}')
"""