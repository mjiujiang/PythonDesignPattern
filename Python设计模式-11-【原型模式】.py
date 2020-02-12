"""
原型模式：用原型实例指定创建对象的种类，并且通过拷贝这些原型创建新的对象。
原型模式本质就是克隆对象，所以在对象初始化操作比较复杂的情况下，很实用，能大大降低耗时，提高性能，因为“不用重新初始化对象，而是动态地获得对象运行时的状态”。

浅拷贝（Shallow Copy）:指对象的字段被拷贝，而字段引用的对象不会被拷贝，拷贝的对象和源对象只是名称相同，但是他们共用一个实体。
深拷贝（deep copy）:对对象实例中字段引用的对象也进行拷贝。
"""
import copy

class Prototype:

    value = 'default'

    def clone(self, **attrs):
        """克隆一个原型，并更新内部属性字典"""
        obj = copy.deepcopy(self)
        obj.__dict__.update(attrs)
        return obj

class PrototypeDispatcher:

    def __init__(self):
        self._objects = {}

    def get_objects(self):
        """获取所有对象"""
        return self._objects

    def register_object(self, name, obj):
        """注册一个对象"""
        self._objects[name] = obj

    def unregister_object(self, name):
        """注销一个对象"""
        del self._objects[name]


def main():
    dispatcher = PrototypeDispatcher()
    prototype = Prototype()

    a = prototype.clone(value='a-value', category='a')
    b = prototype.clone(value='b-value', is_checked=True)
    d = prototype.clone()

    dispatcher.register_object('objecta', a)
    dispatcher.register_object('objectb', b)
    dispatcher.register_object('default', d)
    """
    Python 字典(Dictionary) items() 函数以列表返回可遍历的(键, 值) 元组数组。
    """
    #遍历元组
    #print(dispatcher.get_objects().items())
    print([{n: p.value} for n, p in dispatcher.get_objects().items()])

if __name__ == '__main__':
    main()