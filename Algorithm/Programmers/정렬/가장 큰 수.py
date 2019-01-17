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
    # 각 값을 강제로 4자리수로 만들고 정렬한 뒤 원값을 차곡차곡 넣는다
    
    for i in dic.values():
        
    print(dic)
    return answer