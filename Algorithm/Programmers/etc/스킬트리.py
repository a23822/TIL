"""
미해결
"""

def solution(skill, skill_trees):
    answer = 0
    st = []

    for i in skill_trees:
        temp = []
        for j in i:
            if j in skill:
                temp.append(j)
        st.append(temp)
    print(st)
    
    
    for i in st:
        for j in range(len(i)):
            print("{} 와 {}".format(i, j))
            if i[j] != skill[j]:
                break
            elif j == len(i)-1 and i[j] == skill[j]:
                answer+=1
                print("+=1")
    
    return answer


"""
해결
st 리스트에서 길이가 0 인 경우를 처리 안 했음!!
"""

def solution(skill, skill_trees):
    answer = 0
    st = []

    for i in skill_trees:
        temp = []
        for j in i:
            if j in skill:
                temp.append(j)
        st.append(temp)
    
    
    for i in st:
        if len(i) == 0:
            answer += 1
        for j in range(len(i)):
            if i[j] != skill[j]:
                break
            elif j == len(i)-1 and i[j] == skill[j]:
                answer+=1

    
    return answer