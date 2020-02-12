"""
职责链模式：将能处理请求的对象连成一条链，并沿着这条链传递该请求，直到有一个对象处理请求为止，
避免请求的发送者和接收者之间的耦合关系。
"""
import time
import os
import sys
from contextlib import contextmanager

"""
象处理者：定义出一个处理请求的接口。如果需要，接口可以定义出一个方法，以设定和返回对下家的引用。
这个角色通常是一个抽象类或接口。
"""
class Handler:
    def __init__(self, successor=None):
        self._successor = successor

    def handle(self, request):
        res = self._handle(request)
        if not res:
            self._successor.handle(request)

    def _handle(self, request):
        raise NotImplementedError('必须提供子类实现.')

#实际处理者1
class ConcreteHandler1(Handler):
    def _handle(self, request):
        if 0 < request <= 10:
            print('请求{} 被处理程序1 处理'.format(request))
            return True

#实际处理者2
class ConcreteHandler2(Handler):
    def _handle(self, request):
        if 10 < request <= 20:
            print('请求{} 被处理程序2 处理'.format(request))
            return True

#实际处理者3
class ConcreteHandler3(Handler):
    def _handle(self, request):
        if 20 < request <= 30:
            print('请求{} 被处理程序3 处理'.format(request))
            return True

#默认处理者
class DefaultHandler(Handler):
    def _handle(self, request):
        print('职责链已到终点，没有处理程序处理{}'.format(request))
        return True


"""
   这里用到了yield，然后就可以直接将接收到的数据打印出来了。当然，还有一个值得注意的地方是用到了一个@coroutine的decorator。
   因为在每次使用coroutine之前我们需要调用一次target.next()或者target.send(None)来初始化它。这样我们使用的时候很容易忘记这一步，
   一种办法就是定义好一个这样的decorator，然后每次将这个decorator加上就保证这一步被执行了。@coroutine decorator的定义如下：


   如果是函数定义中参数前的*表示的是将调用时的多个参数放入元组中,**则表示将调用函数时的关键字参数放入一个字典中
    如定义以下函数
    def func(*args):print(args)
    当用func(1,2,3)调用函数时,参数args就是元组(1,2,3)
    定义以下函数

    def func(**args):print(args)
    当用func(a=1,b=2)调用函数时,参数args将会是字典{'a':1,'b':2}
"""
def coroutine(func):
    def start(*args, **kwargs):
        cr = func(*args, **kwargs)
        next(cr)
        return cr
    return start

"""
coroutine是一个实现多个任务之间互相切换的手段，它相当于一种将一个当前执行的结果传递给另外一个过程。
和generator的使用过程比起来，它更像是一种“推”模式。因为我们要使用一个coroutine的时候，必然是需要有其它的过程send数据过来。
因为yield的过程有点类似于一个操作系统里中断的概念，它相当于将一个进程的当前执行过程暂停，然后跳转到另外一个过程。
这种过程和我们传统通过栈实现的子过程调用很不一样，所以表面上理解起来还是有点困难。


因为coroutine相当于一个数据的消费者

协同程序（协程）一般来说是指这样的函数：
    彼此间有不同的局部变量、指令指针，但仍共享全局变量；
    可以方便地挂起、恢复，并且有多个入口点和出口点；
    多个协同程序间表现为协作运行，如A的运行过程中需要B的结果才能继续执行。
"""

@coroutine
def coroutine1(target):
    while True:
        #接收行
        request = yield
        if 0 < request <= 10:
            print('请求{}在被协同程序1 处理 '.format(request))
        else:
            target.send(request)


@coroutine
def coroutine2(target):
    while True:
        request = yield
        if 10 < request <= 20:
            print('请求{}在被协同程序2 处理'.format(request))
        else:
            target.send(request)


@coroutine
def coroutine3(target):
    while True:
        request = yield
        if 20 < request <= 30:
            print('请求{}在被协同程序3 处理'.format(request))
        else:
            target.send(request)


@coroutine
def default_coroutine():
    while True:
        request = yield
        print('职责链的终点，没有协同程序处理{}'.format(request))

"""客户端协程"""
class ClientCoroutine:
    def __init__(self):
        self.target = coroutine1(coroutine3(coroutine2(default_coroutine())))

    def delegate(self, requests):
        for request in requests:
            """发送到下一个阶段"""
            self.target.send(request)


def timeit(func):
    def count(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        count._time = time.time() - start
        return res

    return count

"""上下文管理器（Context Manager）：支持上下文管理协议的对象，这种对象实现了__enter__() 和 __exit__() 方法。上下文管理器定义执行 with 语句时要建立的运行时上下文，负责执行 with 语句块上下文中的进入与退出操作。"""
@contextmanager
def suppress_stdout():
    try:
        stdout, sys.stdout = sys.stdout, open(os.devnull, 'w')
        yield
    finally:
        sys.stdout = stdout




class Client:
    def __init__(self):
        self.handler = ConcreteHandler1(ConcreteHandler3(ConcreteHandler2(DefaultHandler())))

    def delegate(self, requests):
        for request in requests:
            self.handler.handle(request)



if __name__ == "__main__":
    client1 = Client()
    client2 = ClientCoroutine()
    requests = [2, 5, 14, 22, 18, 3, 35, 27, 20]

    client1.delegate(requests)
    print('-' * 30)
    client2.delegate(requests)


    requests *= 10000
    #数组增加到9W个
    #print(requests)
    client1_delegate = timeit(client1.delegate)
    client2_delegate = timeit(client2.delegate)
    with suppress_stdout():
        client1_delegate(requests)
        client2_delegate(requests)
    # 让我们检查哪个速度更快
    print("类处理时间：",client1_delegate._time,"协同程序处理时间：",client2_delegate._time)