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
    temp2 = "("
    while temp:
        p = temp.pop(0)
        if p == "l":
            answer += stack
        elif p == "(":
            if temp2 ==")":
                answer -= stack
            stack += 1
        else: # p == ")"
            if temp2 == "l":
                answer += stack
                stack -= 1
            elif temp2 == "(":
                stack += 1
            elif temp2 == ")":
                stack -= 1

        print("p는 {} temp2는 {}".format(p, temp2))
        temp2 = p
        print(temp)
        print("stack 값은 {} 이고 answer은 {}".format(stack, answer))
    
    return answer