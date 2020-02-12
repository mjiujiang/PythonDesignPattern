"""
代理模式(Proxy)：为某个对象提供一种代理以控制对这个对象的访问。
注意：代理模式和策略模式的类图很相近，实现方法也是一样的，但是应用场景很不一样，体现了不同的思想。
    策略模式中同一外部对象访问上下文对象的操作一样，但是里面的策略对象不同。
    代理模式中不同的外部对象访问代理对象的操作一样，但是里面的真实对象是一样的。
    
代理模式在访问对象时引入一定程度的间接性，因为这种间接性，可以附加多种用途。
应用场景：
1、远程代理。为一个对象在不同的地址空间提供局部代表。这样可以隐藏一个对象存在于不同地址空间的事实。
2、虚拟代理。当要创建耗时很长的对象时，可以使用虚拟代理。虚拟代理完成的工作为新建真实对象，并在新建的过程中给出提示。比如在网页加载图片的过程中，虚拟代理可以用一个图片框暂时替代真实的图片。
3、安全代理。用于控制真实对象访问是的权限。
4、智能指引。当调用真实的对象时，代理处理另外一些事情，比如计算真实对象的引用次数、是否锁定等等。
"""
import time

class SalesManager:
    def talk(self):
        print("销售经理准备谈")

class Proxy:
    def __init__(self):
        self.busy = 'No'
        self.sales = None

    def talk(self):
        print("代理检查销售经理的可访问性")
        if self.busy == 'No':
            self.sales = SalesManager()
            time.sleep(0.1)
            self.sales.talk()
        else:
            time.sleep(0.1)
            print("销售经理正忙")

class NoTalkProxy(Proxy):
    def talk(self):
        print("代理检查销售经理的可访问性")
        time.sleep(0.1)
        print("该销售经理也不会跟你说话不论他/她是否正忙")

if __name__ == '__main__':
    p = Proxy()
    p.talk()
    p.busy = 'Yes'
    p.talk()

    p = NoTalkProxy()
    p.talk()
    p.busy = 'Yes'
    p.talk()