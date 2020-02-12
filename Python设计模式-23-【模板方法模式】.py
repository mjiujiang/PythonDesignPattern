"""
模板方法模式：定义一个操作中的算法的骨架，而将一些步骤延迟到子类中。
因此模板方法使得子类可以在不改变一个算法的结构的情况下重新定义该算法的某些特定变量。
优点：把不变行为搬移到超类，去除子类中的重复代码。
"""
ingredients = "垃圾邮件 鸡蛋 苹果"
line = '-' * 10

# 骨架
def iter_elements(getter, action):
    """模板的骨架-迭代项目"""
    for element in getter():
        action(element)
        print(line)


def rev_elements(getter, action):
    """模板的骨架-反序迭代项目"""
    for element in getter()[::-1]:
        action(element)
        print(line)


def get_list():
    return ingredients.split()


def get_lists():
    return [list(x) for x in ingredients.split()]


def print_item(item):
    print(item)


def reverse_item(item):
    print(item[::-1])


#创建模板
def make_template(skeleton, getter, action):
    """实例化一个模板方法，有 getter 和 action"""
    def template():
        skeleton(getter, action)
    return template

# 创建我们的模板函数
templates = [make_template(s, g, a)
             for g in (get_list, get_lists)
             for a in (print_item, reverse_item)
             for s in (iter_elements, rev_elements)]

# 执行他们
for template in templates:
    template()