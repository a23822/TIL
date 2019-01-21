import csv


lunch = {
        '김밥카페' : '02-1234-5678',
        '양자강': '02-2345-6789',
        '순남시레기' : '02-9851-1234'
    
}
lunch2 = [
    {
        '상호명' : "양자강",
        "전화번호" : "123-1234-1234"
    },
    {
        '상호명' : "김밥카페",
        '전화번호': '02-123-1234'
    },
    {
        "상호명" : '순남시래기',
        '전화번호' : '02-125-1236'
    }

]
menu = ['김밥', '탕수육', '시래기']

# f = open('lunch.csv', 'w')
# for i in lunch:
#     f.write("{}, {} \n".format(i, lunch[i]))
# f.close()

# with open('lunch.csv', 'w') as f:
#     for i in lunch:
#         f.write("{}, {}\n".format(i, lunch[i]))
#         #f.write(", ".join(name, lunch[name])) + '\n')
# f.close()

# with open('lunch.csv', 'w') as f:
#     field = ('상호명', '전화번호')
#     writer = csv.DictWriter(f, fieldnames = field) #필드네임(튜플)"""
#     writer.writeheader()
#     for l in lunch2:
#         writer.writerow(l)
        
with open('lunch.csv', newline = '') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
    