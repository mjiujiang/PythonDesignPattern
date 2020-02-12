"""
迭代器模式：提供一种方法顺序访问一个聚合对象中的各个元素，而又不暴露该对象的内部表示。
一个生成器实现迭代器模式
"""
from __future__ import print_function

def count_to(count):
    """由数字编号计数，最多五个"""
    numbers = ["one", "two", "three", "four", "five"]
    # 枚举（）返回一个包含计数的元组（默认从0开始）从遍历序列获得值
    for pos, number in zip(range(count), numbers):
        yield number

# 测试生成器
count_to_two = lambda: count_to(2)
count_to_five = lambda: count_to(5)

print('数到2...')
for number in count_to_two():
    print(number, end=' ')

print()

print('数到5...')
for number in count_to_five():
    print(number, end=' ')

print()