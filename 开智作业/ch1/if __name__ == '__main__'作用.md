## if __name__ == '__main__'有什么用

``` javascript
if __name__ == '__main__'
```
主要使用目的是为了可以让自己写的这个程序，既可以直接运行，同时也可以当做模块（以文件的形式）被调用
例如：
``` javascript
#文档名字 one.py
def func():
    print("func() in one.py")

print("top-level in one.py")

if __name__ == "__main__":
    func()
    print("one.py is being run directly %s" %__name__)

else:
    print("one.py is being imported into another module %s" %__name__)
```

``` javascript
#文档名为 two.py
import one

print("top-level in two.py")
one.func()

if __name__ == "__main__":
    print("two.py is being run directly %s" %__name__ )
else:
    print("two.py is being imported into another module  %s"  %__name__)
```


运行第一个文档输入：python one.py 结果如下：

``` javascript
top-level in one.py
func() in one.py
one.py is being run directly __main__
```

此时使用时，通过主程序检查（main check），发现直接运行是本程序，所以：1、执行if语句；2、__name__ 显示的是__main__

运行第二个输入：python two.py 结果如下：
``` javascript
top-level in one.py
one.py is being imported into another module one
top-level in two.py
func() in one.py
two.py is being run directly __main__
```

此时，调用了one.py 文件，调用后通过main check，发现one.py文件的程序是通过模块调用执行的，那么one.py文件的里：1、会执行else语句，2、__name__ 显示的是文件名称本身 “one ”

参考：1、https://stackoverflow.com/a/419185  
     2、https://stackoverflow.com/a/419189
     3、https://stackoverflow.com/a/419986
     4、https://stackoverflow.com/a/20158605


