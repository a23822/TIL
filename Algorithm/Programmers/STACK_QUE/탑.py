def solution(heights):
    answer = [0] * len(heights)
    index = len(heights)
    for i in range(1,index+1):
        for j in range(i-1,0,-1):
            #print("{}의 {}임".format(i,j))
            #print("{}와 {}다".format(heights[i-1],heights[j-1]))
            if heights[j-1] > heights[i-1]:
                answer[i-1] = j
                break
    
    return answer