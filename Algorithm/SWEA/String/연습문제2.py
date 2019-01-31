a = input().split()
txt = input()
num_list = [["0", "ZERO"], ["1", "ONE"], ["2", "TWO"], ["3","THREE"], ["4","FOUR"],
    ["5", "FIVE"], ["6", "SIX"], ["7", "SEVEN"], ["8", "EIGHT"], ["9", "NINE"]]
for t in txt:
    if t in a:
        print(t)
        for i in range(len(num_list)):
            if t == num_list[i][0]:
                idx = txt.index(t)
                txt[idx] = num_list[i][1]

                break
print(txt)
