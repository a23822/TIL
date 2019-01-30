a = input()
str_list = ["" for _ in range(len(a))]
for i in range(len(a)):
    str_list[i] = a[i]
answer = ""
for i in range(len(a)-1, -1, -1):
    answer += str_list[i]
print(answer)