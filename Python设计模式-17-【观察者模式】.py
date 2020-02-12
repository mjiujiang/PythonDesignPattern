"""
观察者模式：又叫发布-订阅模式。
    它定义了一种一对多的依赖关系，让多个观察者对象同时鉴定某一个主题对象。这个主题对象在状态发生变化时，
会通知所有的观察者对象，使它们能够自动更新自己。
观察者模式所做的工作实际上就是解耦，根据“依赖倒转原则”，让耦合的双方都依赖于抽象，而不是依赖于具体，
从而使得各自的变化都不会影响另一边的变化。


实际场景中存在的问题：现实中实际观察者不一定有实现观察者的通知回调方法。

解决之道：
1、为其封装一个观察类出来，实现相应的接口。
2、修改通知类，让具体观察者的Notify函数直接去调用相应的接口。
"""
class Subject(object):

    def __init__(self):
        self._observers = []

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self, modifier=None):
        for observer in self._observers:
            if modifier != observer:
                observer.update(self)

#用法示例
class Data(Subject):

    def __init__(self, name=''):
        Subject.__init__(self)
        self.name = name
        self._data = 0

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
        self.notify()

class HexViewer:
    def update(self, subject):
        print('十六进制查看器: 主题 %s 有数据 0x%x' % (subject.name, subject.data))

class DecimalViewer:
    def update(self, subject):
        print('十进制查看器: 主题 %s 有数据 %d' %
              (subject.name, subject.data))

# 用法示例...
def main():
    data1 = Data('Data 1')
    data2 = Data('Data 2')
    view1 = DecimalViewer()
    view2 = HexViewer()
    data1.attach(view1)
    data1.attach(view2)
    data2.attach(view2)
    data2.attach(view1)

    print("设置数据1变量 = 10")
    data1.data = 10
    print("设置数据2变量 = 15")
    data2.data = 15

    print("设置数据1变量 = 3")
    data1.data = 3
    print("设置数据2变量 = 5")
    data2.data = 5

    print("从data1和data2分离HexViewer。")
    data1.detach(view2)
    data2.detach(view2)

    print("设置数据1变量 = 10")
    data1.data = 10
    print("设置数据2变量 = 15")
    data2.data = 15

if __name__ == '__main__':
    main()