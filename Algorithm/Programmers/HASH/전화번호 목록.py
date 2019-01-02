"""
시간초과로 오답
"""

def solution(phone_book):
    
    answer = True
    ing = dict()
    
    # 번호 하나를 선정
    for item in phone_book: 
        index = len(item)
        arr = []
        for i in range(len(phone_book)):
            arr.append(index)
        temp = list(map(lambda x,i: x[:i], phone_book, arr))
        ing[item] = temp
    #print(ing)
    for key, value in ing.items():
        cnt = 0
        for i in value:
            if key == i:
                cnt += 1
        if cnt != 1:
            answer = False
    return answer

"""
여전히 시간초과
"""
def solution2(phone_book):
    
    answer = True
    ing = dict()
    
    # 번호 하나를 선정
    for item in phone_book: 
        index = len(item)
        arr = []
        for i in range(len(phone_book)):
            arr.append(index)
        temp = list(map(lambda x,i: x[:i], phone_book, arr))
        ing[item] = temp
 
    for item in ing.keys():
        temp2 = list(filter(lambda x: x == item, ing[item]))
        if len(temp2) > 1:
            answer = False
            break
    return answer

"""
진행중
"""

def solution(phone_book):
    
    answer = True
    
    #번호 하나를 지정
    for n in phone_book:
        cnt = 0
        arr = phone_book
        arr.remove(n)
        print(arr)
        if n in arr:
            cnt += 1
        print(cnt)
    return answer