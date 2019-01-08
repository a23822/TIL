"""
location 관련해서 계속 실패함
"""


def solution(priorities, location):
    answer = 0
    printing = []
    temp = 0
    while len(priorities) != 1:
        #print("location값은 {} 이다.".format(location))
        # 맨 앞에꺼 뽑는다
        p = priorities.pop(0)
        
        if p >= max(priorities):
            printing.append(p)
            temp+=1
        else: #중요도가 더 높은 문서가 한 개라도 존재할때
            priorities.append(p)    
        print(temp)
    printing.append(priorities[0])
    print(priorities)
    
    print(printing)
    print(location)
    
    return answer