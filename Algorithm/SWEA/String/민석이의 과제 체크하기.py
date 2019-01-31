tc = int(input())

for t in range(tc):
    stud = list(map(int, input().split())) # 학생수/ 제출한 사람 수
    id = list(map(int, input().split()))

    s_list = [i for i in range(1, stud[0]+1)]
    for p in id:
        if p in s_list:
            s_list[s_list.index(p)] = stud[0] + 10
    
    res = [0 for _ in range(stud[0]-stud[1])]
    r = 0
    for a in s_list:
        if a != stud[0] + 10:
            res[r] = a
            r += 1
    res.sort()

    answer = "#{} ".format(t+1)
    for e in res:
        answer += (str(e) + " ")
    
    print(answer[:-1])


    