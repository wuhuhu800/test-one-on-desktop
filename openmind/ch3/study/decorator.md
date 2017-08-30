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
- 含参数的decorator用法：
```javascript
def wap(name1,name2):
    print("^"*20)

    def decorator2(func):
        print("@"*20)
        def dec(*args):
            print('d'*20)
            print(name2)
            print(name1)
            print('pre action')
            result = func(*args)
            print('post action')
            return result
        return dec
    return decorator2

@wap('f2','f5')
def test_f2(name):
    print(name)
    return 'like'

@wap('f3','f4')
def test_f3(name):
    print(name)
    return "dike"

#test_f2('name2')
test_f3('name3')
```
说明：首先会运行@wap('f2','f5')和@wap('f3','f4')的函数的print以及里面的decorator2的print
     然后运行函数test_f3('name3')，由于wap有参数，所以test_f3传给作为decorator2的参数，而
     test_f3的参数name3，传给了decorator2子函数dec的参数。此时注意，在dec函数里的仍然可以
     用wap的参数进行运算。所以此时result = func(* args)就是result = test_f3('name3')
     同样，decorator2函数的返回值就是dec函数的返回值，wap函数的返回值decorator2就是
     deccorator2的返回值dec.

运行结果如下：

```javascript
^^^^^^^^^^^^^^^^^^^^
@@@@@@@@@@@@@@@@@@@@
^^^^^^^^^^^^^^^^^^^^
@@@@@@@@@@@@@@@@@@@@
dddddddddddddddddddd
f4
f3
pre action
name3
post action
返回值：'dike'
```

- 装饰器还可以用到类的函数上
```javascript
def decorator3(func):
    def dec(*args):
        print('pre action')
        result = func(*args)
        print('post action')
        return result
    return dec
​
class Foo:
    @decorator3
    def fun(self):
        print(self)

​
Foo.fun('name1')      
```
运行结果如下：
```javascript
pre action
name1
post actio
```
- 装饰函数的迭代：
对比以下运行结果
```javascript
def decorator4(func):
    print('#'*20)
    def dec(*args):
        print('d4 pre')
        result = func(*args)
        print('d4 post')
        return result
    return dec

def decorator5(func):
    print('-'*20)
    def dec(*args):
        print('d5 pre')
        result = func(*args)
        print('d5 post')
        return result
    return dec

def decorator6(func):
    print('?'*20)
    def dec(*args):
        print('d6 pre')
        result = func(*args)
        print('d6 post')
        return result
    return dec

@decorator4
def test_f4(name):
    print(name +' is good name')
    return 'fly4 away'
@decorator5
def test_f5(name):
    print(name +' is good name')
    return 'fly5 away'
@decorator6
def test_f6(name):
    print(name +' is good name')
    return 'fly6 away'

test_f4('name6')
test_f5('name7')
test_f6('name8')
```
运行结果：（注意前三行的值）
```javascript
####################
--------------------
????????????????????
d4 pre
name6 is good name
d4 post
d5 pre
name7 is good name
d5 post
d6 pre
name8 is good name
d6 post
返回值：fly4 away、fly5 away、fly6 away
```
迭代的装饰器运行函数：
```javascript
def decorator4(func):
    print('#'*20)
    def dec(*args):
        print('d4 pre')
        result = func(*args)
        print('d4 post')
        return result
    return dec

def decorator5(func):
    print('-'*20)
    def dec(*args):
        print('d5 pre')
        result = func(*args)
        print('d5 post')
        return result
    return dec

def decorator6(func):
    print('?'*20)
    def dec(*args):
        print('d6 pre')
        result = func(*args)
        print('d6 post')
        return result
    return dec

@decorator4
@decorator5
@decorator6
def test_f4(name):
    print(name +' is good name')
    return 'fly4 away'

test_f4('name4')
```
说明：我理解的是这样的，运行迭代的装饰器时候，逻辑是先找到迭代里最低级的装饰器层级（@decorator6），
然后运行期里面的程序，但不运行函数，然后再找到更高一级的装饰器（@decorator5），然后运行里面程序，
但不运行函数，最后找到最高级的装饰器（@decorator4），运行里面的程序，然后再运行函数。注意，此时
@decorator4里面的传的参数是decorator5函数这种情况，而dec的参数是@decorator6.test_f4('name4')
所以result = func（*args)是 result = decorator5（@decorator6.test_f4('name4')），
依次类推，decorator5函数子函数dec的result就是 decorator6（test_f4('name4')），
decorator6的子函数dec，result = test_f4('name4')...

运行结果：
```javascript
????????????????????
--------------------
####################
d4 pre
d5 pre
d6 pre
name4 is good name
d6 post
d5 post
d4 post
返回值：fly4 away
```
- 如果装饰器里面有几个并列函数该怎么处理
对比以下例子
```javascript
def decorator1(func):
    def dec(*args1):
        print('pre dec action')
        result1 = func(*args1)
        print('post dec action')
        return result1+' lala'
    print("-"*10)
    def nec(*args2):
        print('pre nec action')
        result2 = func(*args2)
        print('post nec action')
        return result2+' baba'
    return dec

@decorator1
def test_f1(name):
    print(name)
    return 'bike'

test_f1('name1')
```
运行结果
```javascript
----------
pre dec action
name1
post dec action
返回值：
'bike lala'
```
```javascript
def decorator1(func):
    def dec(*args1):
        print('pre dec action')
        result1 = func(*args1)
        print('post dec action')
        return result1+' lala'
    print("-"*10)
    def nec(*args2):
        print('pre nec action')
        result2 = func(*args2)
        print('post nec action')
        return result2+' baba'
    return nec

@decorator1
def test_f1(name):
    print(name)
    return 'bike'

test_f1('name1')

```
运行结果
```javascript
----------
pre nec action
name1
post nec action
Out[98]:
运行结果：'bike baba'
```
说明：装饰器找自己对应的函数是根据装饰器return对应的函数名称寻找应该用哪个函数。装饰器不能同时
返回两个函数，如 return dec，nec是错误的。
部分参考[*** python中decorator的用法及原理（一）***](http://blog.csdn.net/u013696062/article/details/51065406)
