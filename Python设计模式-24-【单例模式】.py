"""
单例模式：保证一个类仅有一个实例，并提供一个访问它的全局访问点。

实现“某个类只有一个实例”途径：
1、让一个全局变量使得一个对象被访问，但是它不能防止外部实例化多个对象。
2、让类自身负责保存它的唯一实例。这个类可以保证没有其他实例可以被创建。即单例模式。

多线程时的单例模式：加锁——双重锁定。

饿汉式单例类：在类被加载时就将自己实例化（静态初始化）。其优点是躲避了多线程访问的安全性问题，缺点是提前占用系统资源。
懒汉式单例类：在第一次被引用时，才将自己实例化。避免开始时占用系统资源，但是有多线程访问安全性问题。
"""

#单例模式
 
def printInfo(info):
    print unicode(info, 'utf-8').encode('gbk')
 
import threading
#单例类
class Singleton():
    instance = None
    mutex = threading.Lock()  
    def __init__(self):
        pass
    
    @staticmethod
    def GetInstance():
        if(Singleton.instance == None):
            Singleton.mutex.acquire() 
            if(Singleton.instance == None):
                printInfo('初始化单例')
                Singleton.instance = Singleton()
            else:
                printInfo('单例已经初始化')  
            Singleton.mutex.release()
        else:
            printInfo('单例已经初始化')        
        return Singleton.instance
 
def main():
    Singleton.GetInstance()
    Singleton.GetInstance()
    Singleton.GetInstance()
    return
 
if __name__ == '__main__':
    main();