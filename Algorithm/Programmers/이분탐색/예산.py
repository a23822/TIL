def solution(budgets, M):
    n_list = []
    sm = min(budgets)
    bg = max(budgets)
    chk = 0
    for b in budgets:
        chk += b
    
    if  chk < M:
        return int(M/len(budgets))
    
    while True:
        temp1 = budgets
        md = int((sm+bg)/2)
        n_list.append(md)
        #print(f'작은건 {sm} 큰건 {bg}')
        n_sum = 0
        for b in temp1:
            if b > md:
                b = md
            n_sum += b
        if n_sum > M:
            bg = md
        elif n_sum < M:
            sm = md
        if sm+1 == bg or sm == bg:
            break
        
    temp2 = budgets
    n_list2 = []
    for n in n_list:
        sum = 0
        for b in temp2:
            if b > n:
                b = n
            sum += b
        n_list2.append(abs(sum-M))
    answer = n_list[n_list2.index(min(n_list2))]
    return answer