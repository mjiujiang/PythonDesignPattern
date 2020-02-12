"""
外观（Facade）模式：为子系统中的一组接口提供一个一致的界面。

——此模式定义了一个高层接口，这个接口使得这一子系统更加容易使用。

与其它模式的区别：与 “简单工厂模式+策略模式”的组合版 很类似，不过外观类的接口不是简单的调用功能类的相应接口，
而是封装成了新的接口。

使用场景：维护一个遗留的大型系统是，可能这个系统已经非常难以维护和扩展，但是它包含很重要的功能，新的开发必须依赖于它，
这样增加外观Facade类，为系统封装一个比较清晰简单的接口，让新系统与Facade对象交互，Facade与遗留代码交互所有复杂的工作
"""
import time

SLEEP = 0.5

# 复杂部分
class TC1:
    def run(self):
        print("###### 测试1 ######")
        time.sleep(SLEEP)
        print(" 设置...")
        time.sleep(SLEEP)
        print("运行测试...")
        time.sleep(SLEEP)
        print("拆除...")
        time.sleep(SLEEP)
        print("测试结束了\n")


class TC2:
    def run(self):
        print("###### 测试2 ######")
        time.sleep(SLEEP)
        print("设置...")
        time.sleep(SLEEP)
        print("运行测试...")
        time.sleep(SLEEP)
        print("拆除...")
        time.sleep(SLEEP)
        print("测试结束了\n")


class TC3:
    def run(self):
        print("###### 测试3 ######")
        time.sleep(SLEEP)
        print(" 设置...")
        time.sleep(SLEEP)
        print("运行测试...")
        time.sleep(SLEEP)
        print("拆除...")
        time.sleep(SLEEP)
        print("测试结束了\n")


# 外观模式
class ExecuteRunner:
    def __init__(self):
        self.tc1 = TC1()
        self.tc2 = TC2()
        self.tc3 = TC3()
        """列表解析
          在一个序列的值上应用一个任意表达式，将其结果收集到一个新的列表中并返回。
          它的基本形式是一个方括号里面包含一个for语句对一个iterable对象迭代"""
        self.tests = [i for i in (self.tc1, self.tc2, self.tc3)]

    def runAll(self):
        [i.run() for i in self.tests]

#主程序
if __name__ == '__main__':
    testrunner = ExecuteRunner()
    testrunner.runAll()