'''
适配器模式：将一个类的接口转换成客户希望的另外一个接口。使得原本由于接口不兼容而不能一起工作的那些类可以一起工作。
应用场景：希望复用一些现存的类，但是接口又与复用环境要求不一致。
分类：类适配器（通过多重继承）、对象适配器。
'''

class Dog(object):
    def __init__(self):
        self.name = "Dog"

    def bark(self):
        return "汪!"


class Cat(object):
    def __init__(self):
        self.name = "Cat"

    def meow(self):
        return "喵!"


class Human(object):
    def __init__(self):
        self.name = "Human"

    def speak(self):
        return "'你好'"


class Car(object):
    def __init__(self):
        self.name = "Car"

    def make_noise(self, octane_level):
        return "引擎声{0}".format("!" * octane_level)


class Adapter(object):

    def __init__(self, obj, **adapted_methods):
        """我们对象字典里设置适配的方法"""
        self.obj = obj
        '''update()方法添加键 - 值对到字典'''
        self.__dict__.update(adapted_methods)


    """我们可以通过重载__getattr__和__setattr__来拦截对成员的访问或者作出一些自己希望的行为
     __getattr__ 在访问对象访问类中不存在的成员时会自动调用"""
    def __getattr__(self, attr):

        return getattr(self.obj, attr ,'没有找到此属性')

    def original_dict(self):
        """输出对象的实例属性"""
        return self.obj.__dict__

def main():
    """定义一个空对象列表"""
    objects = []


    dog = Dog()
    print(dog.__dict__)
    '''追加Adapter实例对象到列表'''
    objects.append(Adapter(dog, make_noise=dog.bark))
    '''Adapter实例属性, 实例也有一个 __dict__特殊属性，它是实例属性构成的一个字典：'''
    '''__dict__ 返回的是一个字典，它的键（key）是属性名，键值（value）是相应的属性对象的数据值'''
    '''实例仅拥有数据属性，它是与某个类的实例相关联的数据值，这些值独立于其他实例或类。当一个实例被释放后，它的属性同时也被清除了。'''
    print(objects[0].__dict__)
    print(objects[0].original_dict())
    print(objects[0].QQ)
    print(objects[0].make_noise())
    print("-----------------------------------------------")

    cat = Cat()
    objects.append(Adapter(cat, make_noise=cat.meow))
    print(objects[1].__dict__)
    print("-----------------------------------------------")

    human = Human()
    objects.append(Adapter(human, make_noise=human.speak))
    print(objects[2].__dict__)
    print("-----------------------------------------------")

    car = Car()
    objects.append(Adapter(car, make_noise=lambda: car.make_noise(5)))
    print(objects[3].__dict__)
    print("-----------------------------------------------")
    for obj in objects:
        print("一个 {0} 正在 {1}".format(obj.name, obj.make_noise()))


if __name__ == "__main__":
        main()