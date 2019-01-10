"""
재귀
"""

def hanoi(n, start, tmp, end):
    
    if n:
        hanoi(n-1, start, end, tmp)
        print("{}번째 원판을, {}에서 {}로".format(n, start, end))
        hanoi(n-1, tmp, start, end)
        
hanoi(4,'a','b','c')