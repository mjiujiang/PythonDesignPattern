# -*- coding: utf-8 -*-
"""
享元模式：运用共享技术有效地支持大量细粒度的对象。
内部状态：享元对象中不会随环境改变而改变的共享部分。比如围棋棋子的颜色。
外部状态：随环境改变而改变、不可以共享的状态就是外部状态。比如围棋棋子的位置。

应用场景：程序中使用了大量的对象，如果删除对象的外部状态，可以用相对较少的共享对象取代很多组对象，就可以考虑使用享元模式。
"""
import weakref

class FlyweightMeta(type):
    def __new__(mcs, name, parents, dct):
        """
        name: 类名
        parents: 父类
        dct: 包括类属性，类方法，静态方法等的字典
        :return:新类
        """

        # 设置实例池
        #创建value为弱引用对象的字典
        dct['pool'] = weakref.WeakValueDictionary()
        return super(FlyweightMeta, mcs).__new__(mcs, name, parents, dct)

    @staticmethod
    def _serialize_params(cls, *args, **kwargs):
        """
        序列化输入参数到key。
        简单的实现仅仅是序列化作为一个字符串
        """
        args_list = map(str, args)
        args_list.extend([str(kwargs), cls.__name__])
        key = ''.join(args_list)
        return key

    """ Python中有一个有趣的语法，只要定义类型的时候，实现__call__函数，这个类型就成为可调用的。
　  换句话说，我们可以把这个类的对象当作函数来使用，相当于重载了括号运算符。"""
    def __call__(cls, *args, **kwargs):
        key = FlyweightMeta._serialize_params(cls, *args, **kwargs)
        """如果cls对象中有属性pool则获取对象，否则设置空字典"""
        pool = getattr(cls, 'pool', {})

        instance = pool.get(key)
        if not instance:
            instance = super(FlyweightMeta, cls).__call__(*args, **kwargs)
            pool[key] = instance
        return instance

class Card(object):

    """
       对象池。内置引用计数
    """
    _CardPool = weakref.WeakValueDictionary()

    """享元模式 实现. 如果池中存在对象就返回它（而不是创建一个新的）"""
    def __new__(cls, value, suit):
        obj = Card._CardPool.get(value + suit)
        if not obj:
            obj = object.__new__(cls)
            Card._CardPool[value + suit] = obj
            obj.value, obj.suit = value, suit
        return obj

    # def __init__(self, value, suit):
    #     self.value, self.suit = value, suit

    def __repr__(self):
        return "<Card: %s%s>" % (self.value, self.suit)


class Card2(object):
    __metaclass__ = FlyweightMeta

    def __init__(self, *args, **kwargs):
        # print('Init {}: {}'.format(self.__class__, (args, kwargs)))
        pass


if __name__ == '__main__':
    import sys
    if sys.version_info[0] > 2:
        sys.stderr.write("!!! This example is compatible only with Python 2 ATM !!!\n")
        raise SystemExit(0)

    #注释__new__ 并取消注释 __init__看出区别
    c1 = Card('9', 'h')
    c2 = Card('9', 'h')
    print(c1, c2)
    print(c1 == c2, c1 is c2)
    print(id(c1), id(c2))

    c1.temp = None
    c3 = Card('9', 'h')
    print(hasattr(c3, 'temp'))
    c1 = c2 = c3 = None
    c3 = Card('9', 'h')
    print(hasattr(c3, 'temp'))

    # 元类 测试
    instances_pool = getattr(Card2, 'pool')
    cm1 = Card2('10', 'h', a=1)
    cm2 = Card2('10', 'h', a=1)
    cm3 = Card2('10', 'h', a=2)

    assert (cm1 == cm2) != cm3
    assert (cm1 is cm2) is not cm3
    assert len(instances_pool) == 2

    del cm1
    assert len(instances_pool) == 2

    del cm2
    assert len(instances_pool) == 1

    del cm3
    assert len(instances_pool) == 0