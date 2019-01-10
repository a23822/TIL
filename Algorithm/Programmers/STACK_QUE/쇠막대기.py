def solution(arrangement):
    answer = 0
    
    """
    ( 들어가고 / ㄹ / ( / 1 / 2 / 3 / ㄹ / ( 3 / ㄹ / ) 2 / ( 2 / ㄹ / 2 / ) 1 / ( 1 / ㄹ / 1
    """
    arr = []
    for i in arrangement:
         arr.append(i)
    temp = []
    while arr:
        p = arr.pop(0)
        if p == "(" and arr[0] == ")":
            del arr[0]
            temp.append("l")
        else:
            temp.append(p)
    print(temp)
    stack = 0
    for i in temp:
        if i == '(':
            stack+=1
        elif i == ')':
            j = temp.index(i)
            if temp[j+1] == '(':
                stack += 1
            elif temp[j+1] == ')':
                stack -= 1
        elif i == 'l':
            answer+= stack
        print(stack)
        
    
    
    return answer