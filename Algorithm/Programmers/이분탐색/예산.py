def solution(budgets, M):
    answer = 0
    n_list = []
    sm = min(budgets)
    bg = max(budgets)
    while True:
        md = int((sm+bg)/2)
        #print(f'작은건 {sm} 큰건 {bg}')
        n_sum = 0
        for b in budgets:
            if b > md:
                b = md
            n_sum += b
        if n_sum > M:
            bg = md
        elif n_sum < M:
            sm = md
        if sm+1 == bg:
            break
        elif sm == bg:
            break
        n_list.append(md)
    #print(n_list)
    return n_list[-1]