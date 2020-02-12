"""
工厂模式：根据传入参数的不同, 而返回对应的对象
"""

class ChineseGetter:
    """具体工厂类"""

    def __init__(self):
        self.trans = dict(dog="狗", cat="猫",parrot="鹦鹉",bear="熊")

    def get(self, msgid):
        """如果我们没有一个翻译，我们会把"""
        return self.trans.get(msgid, str(msgid))


class EnglishGetter:

    """简单地输出了消息ID"""

    def get(self, msgid):
        return str(msgid)


def get_localizer(language="English"):
    """工厂方法"""
    languages = dict(English=EnglishGetter, Chinese=ChineseGetter)
    return languages[language]()

if __name__ == "__main__":
    #创建本地化
    e, c= get_localizer(language="English"), get_localizer(language="Chinese")

    # 本地化一些文本
    for msgid in "dog parrot cat bear".split():
        print("english:"+e.get(msgid),"中文:"+c.get(msgid))
