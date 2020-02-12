"""
组合模式，将对象组合成树形结构以表示“部分-整体”的层次结构，组合模式使得用户对单个对象和组合对象的使用具有一致性。"""

"""
一个类定义的组合对象，它可以用名称来存储分层使用的字典。

这个类是相同的分层字典，但它按名称提供方法来添加/访问/修改子元素，就像一个组合。

"""

def normalize(val):
    """ 正常化一个特殊字符的字符串，以便它可以被用来作为一个Python对象一个属性
    """

    if val.find('-') != -1:
        val = val.replace('-', '_')

    return val


def denormalize(val):
    """ 非规范化一个字符串"""

    if val.find('_') != -1:
        val = val.replace('_', '-')

    return val


class SpecialDict(dict):

    """
    字典类，允许其键直接访问属性
    """

    def __getattr__(self, name):

        if name in self.__dict__:
            return self.__dict__[name]
        elif name in self:
            return self.get(name)
        else:
            # 检查非规范化的名字
            name = denormalize(name)
            if name in self:
                return self.get(name)
            else:
                raise AttributeError('没有属性名称 %s' % name)

    def __setattr__(self, name, value):

        if name in self.__dict__:
            self.__dict__[name] = value
        elif name in self:
            self[name] = value
        else:
            # 检查非规范化的名字
            name2 = denormalize(name)
            if name2 in self:
                self[name2] = value
            else:
                # 新属性
                self[name] = value


class CompositeDict(SpecialDict):

    """一类像一个层次词典。
    这个类是基于组合设计模式"""

    ID = 0

    def __init__(self, name=''):

        if name:
            self._name = name
        else:
            self._name = ''.join(('id#', str(self.__class__.ID)))
            self.__class__.ID += 1

        self._children = []
        # 链接到父亲
        self._father = None
        self[self._name] = SpecialDict()

    def __getattr__(self, name):

        if name in self.__dict__:
            return self.__dict__[name]
        elif name in self:
            return self.get(name)
        else:
            #  检查非规范化的名字
            name = denormalize(name)
            if name in self:
                return self.get(name)
            else:
                #查看孩子列表
                child = self.findChild(name)
                if child:
                    return child
                else:
                    attr = getattr(self[self._name], name)
                    if attr:
                        return attr

                    raise AttributeError('no attribute named %s' % name)

    def isRoot(self):
        """ Return 我是否根组件"""

        # 如果我没有父母，我的根节点
        return not self._father

    def isLeaf(self):
        """ Return 叶节点 """

        # 我是一片叶节点，如果我没有孩子
        return not self._children

    def getName(self):
        """ 返回ConfigInfo对象的名称 """

        return self._name

    def getIndex(self, child):
        """返回孩子ConfigInfo对象的'child'的索引"""

        if child in self._children:
            return self._children.index(child)
        else:
            return -1

    def getDict(self):
        """ 返回包含的词典"""

        return self[self._name]

    def getProperty(self, child, key):
        """ 返回属性值"""

        # 首先get孩子的字典
        childDict = self.getInfoDict(child)
        if childDict:
            return childDict.get(key, None)

    def setProperty(self, child, key, value):
        """
        设置属性的“key”的值
        """

        #首先get孩子的字典
        childDict = self.getInfoDict(child)
        if childDict:
            childDict[key] = value

    def getChildren(self):
        """ 返回此对象的直接子列表 """

        return self._children

    def getAllChildren(self):
        """ 返回此对象的所有子列表 """

        l = []
        for child in self._children:
            l.append(child)
            l.extend(child.getAllChildren())

        return l

    def getChild(self, name):
        """
         用给定名称返回直接子对象
        """

        for child in self._children:
            if child.getName() == name:
                return child

    def findChild(self, name):
        """
            从树返回(用给定的名称)子对象
        """

        # 这将返回给定名称的第一个子对象
        #任何其他具有类似名称的子对象不被考虑
        for child in self.getAllChildren():
            if child.getName() == name:
                return child

    def findChildren(self, name):
        """ 从树返回给定名称的子对象列表"""

        #这将返回给定名称的所有子项的列表，不论查询的深度
        children = []

        for child in self.getAllChildren():
            if child.getName() == name:
                children.append(child)

        return children

    def getPropertyDict(self):
        """ 返回属性字典"""

        d = self.getChild('__properties')
        if d:
            return d.getDict()
        else:
            return {}

    def getParent(self):

        return self._father

    def __setChildDict(self, child):
        """
        私有方法来设置子对象的'child'的字典在内部字典
        """

        d = self[self._name]
        d[child.getName()] = child.getDict()

    def setParent(self, father):

        self._father = father

    def setName(self, name):
        """
            设置此ConfigInfo对象的名称为'name'
        """

        self._name = name

    def setDict(self, d):
        self[self._name] = d.copy()

    def setAttribute(self, name, value):
        self[self._name][name] = value

    def getAttribute(self, name):
        return self[self._name][name]

    def addChild(self, name, force=False):
        """
        添加一个新的子节点
        如果可选标志“force”设置为True，子对象被覆盖，如果它已经存在。
        该函数返回子对象，无论是新的或现有的
        """

        if type(name) != str:
            raise ValueError('Argument should be a string!')

        child = self.getChild(name)
        if child:
            # print('Child %s present!' % name)
            # 如果force==True 更换它
            if force:
                index = self.getIndex(child)
                if index != -1:
                    child = self.__class__(name)
                    self._children[index] = child
                    child.setParent(self)

                    self.__setChildDict(child)
            return child
        else:
            child = self.__class__(name)
            child.setParent(self)

            self._children.append(child)
            self.__setChildDict(child)

            return child

    def addChild2(self, child):
        """
        添加子对象'child'。如果它已经存在，它由缺省覆盖
        """
        currChild = self.getChild(child.getName())
        if currChild:
            index = self.getIndex(currChild)
            if index != -1:
                self._children[index] = child
                child.setParent(self)
                # 未设置现有的子节点的父级
                currChild.setParent(None)
                del currChild

                self.__setChildDict(child)
        else:
            child.setParent(self)
            self._children.append(child)
            self.__setChildDict(child)


if __name__ == "__main__":
    window = CompositeDict('Window')
    frame = window.addChild('Frame')
    tfield = frame.addChild('Text Field')
    tfield.setAttribute('size', '20')

    btn = frame.addChild('Button1')
    btn.setAttribute('label', '提交')

    btn = frame.addChild('Button2')
    btn.setAttribute('label', '浏览')

    #print(window)
    #print(window.Frame)
    #print(window.Frame.Button1)
    #print(window.Frame.Button2)
    print(window.Frame.Button1.label)
    print(window.Frame.Button2.label)