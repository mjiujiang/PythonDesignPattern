"""
中介者模式：用一个中介对象来封装一系列的对象交互。中介者使各对象不需要显式地相互引用，从而使其耦合松散，
而且可以独立地改变它们之间的交互。
一般应用于一组对象以定义良好但是复杂的方式进行通信的场合。
优点：降低了各个模块的耦合性。
缺点：中介对象容易变得复杂和庞大。
"""
# -*- coding: utf-8 -*-
import random
import time

class TC:
    def __init__(self):
        self._tm = None
        self._bProblem = 0

    def setup(self):
        print("设置测试")
        time.sleep(0.1)
        self._tm.prepareReporting()

    def execute(self):
        if not self._bProblem:
            print("执行测试")
            time.sleep(0.1)
        else:
            print("问题设置。测试不执行。")

    def tearDown(self):
        if not self._bProblem:
            print("拆除")
            time.sleep(0.1)
            self._tm.publishReport()
        else:
            print("测试不执行。没有拆除需要")

    def setTM(self, tm):
        self._tm = tm

    def setProblem(self, value):
        self._bProblem = value

class Reporter:
    def __init__(self):
        self._tm = None

    def prepare(self):
        print("报表类正准备报告结果")
        time.sleep(0.1)

    def report(self):
        print("报告测试的结果")
        time.sleep(0.1)

    def setTM(self, tm):
        self._tm = tm

class DB:
    def __init__(self):
        self._tm = None

    def insert(self):
        print("增加执行开始状态在数据库")
        time.sleep(0.1)
        # 下面的代码是模拟从DB到TC通信
        if random.randrange(1, 4) == 3:
            return -1

    def update(self):
        print("更新数据库中的测试结果")
        time.sleep(0.1)

    def setTM(self, tm):
        self._tm = tm

class TestManager:

    def __init__(self):
        self._reporter = None
        self._db = None
        self._tc = None

    def prepareReporting(self):
        rvalue = self._db.insert()
        if rvalue == -1:
            self._tc.setProblem(1)
            self._reporter.prepare()

    def setReporter(self, reporter):
        self._reporter = reporter

    def setDB(self, db):
        self._db = db

    def publishReport(self):
        self._db.update()
        self._reporter.report()

    def setTC(self, tc):
        self._tc = tc

if __name__ == '__main__':
    reporter = Reporter()
    db = DB()
    tm = TestManager()
    tm.setReporter(reporter)
    tm.setDB(db)
    reporter.setTM(tm)
    db.setTM(tm)
    #为了简化，我们在相同的测试循环。
    #实际上，它可能是有关各种独特的测试类和它们的对象
    for i in range(3):
        tc = TC()
        tc.setTM(tm)
        tm.setTC(tc)
        tc.setup()
        tc.execute()
        tc.tearDown()