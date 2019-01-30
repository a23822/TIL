tc = int(input())
t_list = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
for t in range(tc):
    N = int(input().split()[1])
    a = input().split()
    n_list = [0]*10
    for i in a:
        if i in t_list:
            n_list[t_list.index(i)] += 1
    answer = ""
    for i in range(len(n_list)):
        answer+=(t_list[i] + " ")*n_list[i]
    print("#{}".format(t+1))
    print(answer[:-1])