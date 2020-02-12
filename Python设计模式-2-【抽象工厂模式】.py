"""
抽象工厂模式：提供一个创建一系列相关或相互依赖对象的接口，而无需指定它们具体的类。

优点：易于交换“产品系列”，只要更改相应的工厂即可。
缺点：建立产品的时候很繁琐，需要增加和修改很多东西。

优化1：为了避免客户端有过多的逻辑判断，可以封装出一个简单工厂类来生成产品类。
优化2：为了减少简单工厂类里面的逻辑判断，可以采用“反射”机制，直接根据外部的配置文件读取出需要使用产品类的信息。
"""

"""抽象工厂模式的实现"""

import random


class PetShop:

    """宠物商店"""

    def __init__(self, animal_factory=None):

        """宠物工厂是我们的抽象工厂。我们可以随意设置。""" 
        self.pet_factory = animal_factory

    def show_pet(self):

        """使用抽象工厂创建并显示一个宠物"""

        pet = self.pet_factory.get_pet()
        print("我们有一个可爱的 {}".format(pet))
        print("它说 {}".format(pet.speak()))
        print("我们还有 {}".format(self.pet_factory.get_food()))


# 工厂生产的事物

class Dog:

    def speak(self):
        return "汪"

    def __str__(self):
        return "Dog"


class Cat:

    def speak(self):
        return "喵"

    def __str__(self):
        return "Cat"


# Factory classes

class DogFactory:

    def get_pet(self):
        return Dog()

    def get_food(self):
        return "狗食"


class CatFactory:

    def get_pet(self):
        return Cat()

    def get_food(self):
        return "猫粮"


# 随机创建合适的工厂
def get_factory():
    """让我们动起来！"""
    return random.choice([DogFactory, CatFactory])()


# 多个工厂显示宠物
if __name__ == "__main__":
    for i in range(4):
        shop = PetShop(get_factory())
        shop.show_pet()
        print("=" * 20)
