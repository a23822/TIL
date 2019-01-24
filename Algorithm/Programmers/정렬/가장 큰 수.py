def solution(numbers):
    answer = ''
    temp = list(map(str, numbers))
    dic = {}
    # 첫 자리수에 따라 dic 에 삽입
    for i in temp:
        if int(i[0]) in dic.keys():
            dic[int(i[0])].append(i)
        else:
            dic[int(i[0])] = [i]
    li = sorted(dic.items(), reverse=True)
    
    for i in range(len(li)):
        comp = []
        ref = []
        for j in li[i][1]:
            comp.append(int(j+str(li[i][0])*(4-len(j))))
            ref.append(4-len(j))

        while comp:
            ref_p = ref.pop(comp.index(max(comp)))
            p = comp.pop(comp.index(max(comp)))
            p = int(p/10**ref_p)
            answer+=str(p)
    return answer