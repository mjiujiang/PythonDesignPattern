"""
桥接模式：将系统抽象部分与它的实现部分分离，使它们可以独立地变化。
由于目标系统存在多个角度的分类，每一种分类都会有多种变化，那么就可以把多角度分离出来，让它们独立变化，减少它们之间的耦合。
"""

# 具体实现者1/2
class DrawingAPI1(object):

    def draw_circle(self, x, y, radius):
        print('API1.circle at {}:{} 半径 {}'.format(x, y, radius))


# 具体实现者2/2
class DrawingAPI2(object):

    def draw_circle(self, x, y, radius):
        print('API2.circle at {}:{} 半径 {}'.format(x, y, radius))

# 优雅的抽象
class CircleShape(object):

    def __init__(self, x, y, radius, drawing_api):
        self._x = x
        self._y = y
        self._radius = radius
        self._drawing_api = drawing_api

    # 低层次的，即具体的的实现
    def draw(self):
        self._drawing_api.draw_circle(self._x, self._y, self._radius)

    # 高层次的抽象
    def scale(self, pct):
        self._radius *= pct


def main():
    shapes = (
        CircleShape(1, 2, 3, DrawingAPI1()),
        CircleShape(5, 7, 11, DrawingAPI2())
    )

    for shape in shapes:
        '''坐标--缩放变换'''
        shape.scale(2.5)
        shape.draw()

if __name__ == '__main__':
    main()
