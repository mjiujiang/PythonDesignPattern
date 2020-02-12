"""
命令模式：将一个请求封装为一个对象，从而使你可用不同的请求对客户进行参数化；
支持对请求排队、记录请求日志，以及可撤销的操作。

优点：把请求一个操作的对象与知道怎么执行一个操作的对象分隔开。
"""

import os
from os.path import lexists

class MoveFileCommand(object):

    def __init__(self, src, dest):
        self.src = src
        self.dest = dest

    def execute(self):
        self.rename(self.src, self.dest)

    def undo(self):
        self.rename(self.dest, self.src)

    def rename(self, src, dest):
        print('重命名 {} to {}'.format(src, dest))

        """
        os.rename() 方法用于命名文件或目录，从 src 到 dst,如果dst是一个存在的目录, 将抛出OSError。
        src -- 要修改的目录名
        dst -- 修改后的目录名
        """
        os.rename(src, dest)


def main():
    command_stack = []

    # 命令只是压入命令栈
    command_stack.append(MoveFileCommand('foo.txt', 'bar.txt'))
    command_stack.append(MoveFileCommand('bar.txt', 'baz.txt'))

    # 确认没有任何目标文件的存在
    assert(not lexists("foo.txt"))
    assert(not lexists("bar.txt"))
    assert(not lexists("baz.txt"))
    try:
        with open("foo.txt", "w"):  # 创建文件
            pass

        #它们可以稍后执行
        for cmd in command_stack:
            cmd.execute()

        #并且也可以随意撤消
        """
        reversed()倒排列表中的元素
        """
        for cmd in reversed(command_stack):
            cmd.undo()
    finally:
        """
        os.unlink() 方法用于删除文件,如果文件是一个目录则返回一个错误。
        """
        os.unlink("foo.txt")

if __name__ == "__main__":
    #print("目录为: %s" % os.listdir(os.getcwd()))

    main()