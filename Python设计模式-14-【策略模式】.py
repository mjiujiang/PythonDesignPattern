"""
策略模式是一种定义一系列算法的方法，从概念上，所有这些算法完成的都是相同的工作，只是实现不同。
所以可以实现context类，他可以以相同的方式调用所有的算法，减少了各类算法类与使用算法类之间之间的耦合。
"""
import types

class StrategyExample:
    def __init__(self, func=None):
        self.name = '策略例子0'
        if func is not None:
            """给实例绑定方法用的，不会影响到其他实例"""
            self.execute = types.MethodType(func, self)

    def execute(self):
        print(self.name)

def execute_replacement1(self):
    print(self.name + ' 从执行1')


def execute_replacement2(self):
    print(self.name + ' 从执行2')


if __name__ == '__main__':
    strat0 = StrategyExample()

    strat1 = StrategyExample(execute_replacement1)
    strat1.name = '策略例子1'

    strat2 = StrategyExample(execute_replacement2)
    strat2.name = '策略例子2'

    strat0.execute()
    strat1.execute()
    strat2.execute()