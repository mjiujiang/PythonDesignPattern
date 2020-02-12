"""
建造者模式：将一个复杂对象的构建与它的表示分离，使得同样的构建过程可以创建不同的表示。
相关模式：思路和模板方法模式很像，模板方法是封装算法流程，对某些细节，
提供接口由子类修改，建造者模式更为高层一点，将所有细节都交由子类实现。
"""
#主管者，构造一个使用Builder接口的对象
#调用具体建造者来创建复杂对象的各个部分，在指导者中不涉及具体产品的信息，只负责保证对象各部分完整创建或按某种顺序创建。
class Director(object):
    def __init__(self):
        self.builder = None

    def construct_building(self):
        #实例化BuildProduct类,self.building = None变成self.building = BuildProduct()
        self.builder.new_building()

        self.builder.build_floor()
        self.builder.build_size()

    def get_building(self):
        return self.builder.building


# 抽象构建器
#给出一个抽象接口，以规范产品对象的各个组成成分的建造。这个接口规定要实现复杂对象的哪些部分的创建，并不涉及具体的对象部件的创建。
class Builder(object):
    def __init__(self):
        self.building = None

    #新的创建者
    def new_building(self):
        self.building = BuildProduct()

    def build_floor(self):
        raise NotImplementedError

    def build_size(self):
        raise NotImplementedError

#实现构建器
#实现Builder接口，针对不同的商业逻辑，具体化复杂对象的各部分的创建。 在建造过程完成后，提供产品的实例。
class BuilderHouse(Builder):

    def build_floor(self):
        self.building.floor = '一'

    def build_size(self):
        self.building.size = '大'


class BuilderFlat(Builder):

    def build_floor(self):
        self.building.floor = '超过一层'

    def build_size(self):
        self.building.size = '小'

# 要创建的复杂对象的产品类。
class BuildProduct(object):

    def __init__(self):
        self.floor = None
        self.size = None

    """Python中这个_repr_函数，对应repr(object)这个函数，返回一个可以用来表示对象的可打印字符串"""
    def __repr__(self):
        return '楼层: {0.floor} | 尺寸: {0.size}'.format(self)


#程序主入口
if __name__ == "__main__":
    director = Director()
    #具体实现类实例化抽象接口，并赋值给Director对象里builder属性
    director.builder = BuilderHouse()
    #调用Director对象的construct_building方法,实际是执行BuilderHouse(builder属性)对象的3个方法
    director.construct_building()
    #得到BuildProduct对象
    building = director.get_building()
    #打印对象字符串
    print(building)

    director.builder = BuilderFlat()
    director.construct_building()
    building = director.get_building()
    print(building)