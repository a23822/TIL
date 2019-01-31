for _ in range(10):
    t = int(input())
    t_list = ["" for _ in range(200)]
    for i in range(100):
        t_list[i] = input()
    for j in range(100):
        temp = ""
        for k in range(100):
            temp += t_list[k][j]
        t_list[100+j] = temp
    
    longest = 1
    for txt in t_list:
        tp = 0
        for first in range(100):
            for second in range(100-first+1):
                if txt[first:first+second] == txt[first:first+second][::-1]:
                    tp = len(txt[first:first+second])
                if tp > longest:
                    longest = tp
    
    print("#{} {}".format(t, longest))


"""
다른사람 풀이
"""

for i in range(1,11):
    str_arr=[[] for a in range(100)]
    tc = input()
    for a in range(100):
        str_arr[a]= input()
 
    m=25
    #
    flag=0
    while m>0:
        for a in range(100):
            for c in range(100-m+1):
                for b in range(c,m//2+c):
                    if str_arr[a][b]!=str_arr[a][m+2*c-b-1]:
                        break
                else :
                    flag = 1
                    break
                    break
 
 
        if flag==0:
            for a in range(100):
                for c in range(100 - m+1):
                    for b in range(c,m//2+c):
                        if str_arr[b][a] != str_arr[m+2*c-b-1][a]:
                            break
                    else:
                        flag=1
                        break
                        break
        else:
            break
        if flag==1:
            break
        m-=1
 
    print(f"#{i} {m}")