"""
共享模式：
"""
# 共享模式
class Borg:
    """共享状态"""
    __shared_state = {}

    def __init__(self):
        self.__dict__ = self.__shared_state
        self.state = '初始化'

    """当你打印一个类的时候，那么print首先调用的就是类里面的定义的__str__"""
    """当打印Borg的一个实例的时候，__str__函数被调用到"""
    def __str__(self):
        return self.state

class YourBorg(Borg):
    """Python pass是空语句，是为了保持程序结构的完整性。
       pass 不做任何事情，一般用做占位语句。"""
    pass

if __name__ == '__main__':
    rm1 = Borg()
    rm2 = Borg()

    rm1.state = '空闲的'
    rm2.state = '运行中的'

    print('rm1: {0}'.format(rm1))
    print('rm2: {0}'.format(rm2))

    """改变（共享的）状态"""
    rm2.state = '僵尸'

    print('rm1: {0}'.format(rm1))
    print('rm2: {0}'.format(rm2))

    print('rm1 id: {0}'.format(id(rm1)))
    print('rm2 id: {0}'.format(id(rm2)))

    """初始化（共享的）状态"""
    rm3 = YourBorg()

    print('rm1: {0}'.format(rm1))
    print('rm2: {0}'.format(rm2))
    print('rm3: {0}'.format(rm3))