*args 를 쓰면 튜플형태로 들어옴

여러 개의 인자를 받을 수가 있다.

밑에는 그 예제

``` python
def my_mul(*args):
    res = 1
    for i in args:
        res *= i
    return res

print(my_mul(6))
print(my_mul(3,5))
```



**kwargs

는 keyword argument의 줄임말로 키워드를 제공함

``` python
def ie(**kwargs):
    for key, value in kwargs.items():
        print("{} is {}".format(key,value))
        
ie(myName = 'Chris')

# myName is Chris
```

