def solution(array, commands):
    answer = []
    for i in commands:
        answer.append(list(sorted(array[i[0]-1:i[1]]))[i[2]-1])
    return answer

"""
더 줄일 수 있었다...
"""
def solution2(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))