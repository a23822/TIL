#movies = ['1','2','3','4','5','6','7']
content = "this is content"

# f = open('a.txt', 'w')
# f.write("wow this if file!" + "\n")
# #print(dir(f))
# f = open('a.txt', 'r')
# print(f.read())
# f = open('movie.txt' , 'w')
# for movie in movies:
#     f.write(movie + ',')
# f.close()
movies = []
f = open('movie.txt', 'r')
movies = f.read().split(",")
print(movies)
f.close()