"""
状态模式：当一个对象的内在状态改变时允许改变其行为，这个对象看起来像是改变了其类。
应用场景：一个对象的行为取决于它的状态，即它必须在运行时刻根据状态改变它的行为。
如果控制状态转换的条件表达式过于复杂，就可以考虑使用状态模式。

关键点：把状态的判断逻辑转移到表示不同状态的一系列类当中，这样就可以简化复杂的逻辑判断了。
优点：将与特定状态相关的行为局部化，并且将不同状态的行为分割开来。
"""
from __future__ import print_function

class State(object):
    """基本状态。这是共享的功能"""
    def scan(self):
        """扫描拨盘到下一状态"""
        self.pos += 1
        if self.pos == len(self.stations):
           self.pos = 0
        print("扫描... 状态是", self.stations[self.pos], self.name)

class AmState(State):

    def __init__(self, radio):
        self.radio = radio
        self.stations = ["1250", "1380", "1510"]
        self.pos = 0
        self.name = "AM"

    def toggle_amfm(self):
        print("切换到FM...")
        self.radio.state = self.radio.fmstate


class FmState(State):

    def __init__(self, radio):
        self.radio = radio
        self.stations = ["81.3", "89.1", "103.9"]
        self.pos = 0
        self.name = "FM"

    def toggle_amfm(self):
        print("切换到AM...")
        self.radio.state = self.radio.amstate

class Radio(object):

    """一台收音机。它有一个扫描按钮，和一个AM / FM切换开关。"""

    def __init__(self):
        """我们有一个AM状态和FM状态"""
        """AmState继承了State"""
        self.amstate = AmState(self)
        self.fmstate = FmState(self)
        """初始化am状态"""
        self.state = self.amstate

    def toggle_amfm(self):
        self.state.toggle_amfm()

    def scan(self):
        self.state.scan()

# 测试入口
if __name__ == '__main__':
    radio = Radio()
    actions = [radio.scan] * 2 + [radio.toggle_amfm] + [radio.scan] * 2
    actions *= 2

    for action in actions:
        action()