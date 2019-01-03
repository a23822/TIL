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
괜히 복잡하게 생각함
"""

def solution3(phone_book):
    
    for i in range(len(phone_book)):
        item = phone_book[i]
        index = len(item)
        cnt = 0
        for j in range(len(phone_book)):
            item2 = phone_book[j]
            #print("1번:"+item+"  2번:"+item2[:index])
            if item == item2[:index]:
                cnt += 1
        if cnt > 1:
            return False
    return True

"""
일반적인 다른사람들의 풀이
"""

def solution4(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)):
        for j in range(len(phone_book)-i-1):
            if phone_book[i] in phone_book[j+i+1]:
                return False
    return True

"""
regex??
"""

import re
def solution5(phoneBook):

    for b in phoneBook:
        p = re.compile("^"+b)
        for b2 in phoneBook:
            if b != b2 and p.match(b2):
                return False
    return True

"""
string 정렬, 간단하지만 효율성테스트에서 느리다고 함.
"""
def solution6(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True


"""
???
"""

from itertools import combinations as c
def solution7(phoneBook):
    answer = True
    sortedPB = sorted(phoneBook, key= len)
    for (a,b) in c( sortedPB,2):
        if a == b[:len(a)]:
            answer = False
    return answer