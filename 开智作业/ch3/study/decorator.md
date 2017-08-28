### decorator函数初步探索
decorator 函数装饰器，将函数进行封装，目的是在调用函数之前和之后搞点事情，大概有以下几种用法：
- 不带参数的decorator用法：
```javascript
def decorator1(func):
    def dec(*args):
        print('pre action')
        result = func(*args)
        print('post action')
        return result+' lala'
    return dec

@decorator1 #调用函数装饰器
def test_f1(name):
    print(name)
    return 'bike'

test_f1('name1')
```
说明：@decorator1
     def test_f1(name):
     相当于test_f1 = decorator1(test_f1），当调用test_f1（‘name1’）的时候，调用了
     decorator（test_f1),将test_f1作为参数传给了函数decorator，test_f1的参数name1
     传给了decorator的子函数dec的参数*args，而result=func(* args) 的实际就是执行
     result = test_f1('name1'),即func就是test_f1,* args 就是name1
     dec 的函数return 没有任何要求，可以是任何形式，但是decorator1的函数return必须是
     其底下子函数名称之一，后面例子会进一步说明。这样return dec的话其实就是dec函数的返回值
     return（即本例result+' lala'）


运行结果:
```javascript
pre action
name1
post action
返回值 'bike lala'
```
