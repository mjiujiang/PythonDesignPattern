"""
装饰模式：动态地给一个对象添加一些额外的职责，就增加功能来说，装饰模式比生成子类更为灵活。
应用场景：适用于 "新加入的功能仅仅是为了满足一些只在某些特定情况下才会执行的需求“。
优点：
1、把类中的装饰功能从类中去除，简化原有的类。
2、装饰模式把每个要装饰的功能放在单独的装饰类中，并让这个装饰类包装它所要装饰的对象。因此，当需要执行特殊行为时，
客户代码就可以在运行时根据需要有选择地、按顺序地使用装饰功能包装对象。
"""

from functools import wraps

#装饰器makebold
def makebold(fn):
    return getwrapped(fn, "b")

#装饰器makeitalic
def makeitalic(fn):
    return getwrapped(fn, "i")

def getwrapped(fn, tag):
    """装饰器是一个函数，其主要用途是包装另一个函数或类。这种包装的首要目的是透明地修改或增强被包装对象的行为。"""
    @wraps(fn)
    def wrapped():
        return "<%s>%s</%s>" % (tag, fn(), tag)

    # 结果返回该函数
    return wrapped


@makebold
@makeitalic
def hello():
    """装饰的Hello World"""
    return "hello world"

if __name__ == '__main__':
    """每个函数都是一个对象，每个函数对象都是有一个__doc__的属性，函数语句中，
       如果第一个表达式是一个string，这个函数的__doc__就是这个string，否则__doc__是None。
    """
    print('  返回结果:{} \r\n  获取函数名:{}  \r\n  对函数/方法/模块所实现功能的简单描述:{}'.format(hello(), hello.__name__, hello.__doc__))