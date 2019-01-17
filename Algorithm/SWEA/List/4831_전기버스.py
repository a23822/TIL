T = int(input()) # 노선 수
for n in range(T):
    temp = list(map(int, input().split())) # 최대이동거리 K,, 종점 N , 충전기 M
    cs = list(map(int, input().split())) # 충전기가 설치된 정류장 번호
    cnt = 0 # 충전횟수
    pos = 0 # 버스 위치
    c_idx = 0 # 충전기 인덱스

    while pos+temp[0] < temp[1]:
        ref = 0
        ref2 = 0
        for i in range(c_idx, len(cs)):
            if pos + temp[0] >= cs[i]:
                ref = cs[i]
                ref2 += 1
                continue
            else:
                c_idx+=1
                break
        if ref2 == 0:
            cnt = 0
            break
        pos = ref
        cnt += 1
    

    print(f'#{n+1} {cnt}')