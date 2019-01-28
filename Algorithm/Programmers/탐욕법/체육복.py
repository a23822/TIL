def solution(n, lost, reserve):
    lost_num = len(lost)
    cnt = 0
    temp = []
    while reserve:
        p = reserve.pop(0)
        if p+1 in lost:
            temp.append(p+1)
            cnt+=1
        if p-1 in lost:
            temp.append(p-1)
            cnt+=1
    print(temp)
    
    return n-lost_num+cnt