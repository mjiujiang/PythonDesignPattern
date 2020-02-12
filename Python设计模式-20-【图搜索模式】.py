class GraphSearch:
    """
    在python模拟图搜索模式
    """
    def __init__(self, graph):
        self.graph = graph

    def find_path(self, start, end, path=None):
        path = path or []

        path.append(start)
        if start == end:
            return path
        for node in self.graph.get(start, []):
            if node not in path:
                newpath = self.find_path(node, end, path)
                if newpath:
                    return newpath

    def find_all_path(self, start, end, path=None):
        path = path or []
        path.append(start)
        if start == end:
            return [path]
        paths = []
        for node in self.graph.get(start, []):
            if node not in path:
                newpaths = self.find_all_path(node, end, path[:])
                paths.extend(newpaths)
        return paths

    def find_shortest_path(self, start, end, path=None):
        path = path or []
        path.append(start)

        if start == end:
            return path
        shortest = None
        for node in self.graph.get(start, []):
            if node not in path:
                newpath = self.find_shortest_path(node, end, path[:])
                if newpath:
                    if not shortest or len(newpath) < len(shortest):
                        shortest = newpath
        return shortest

#图用法的例子
graph = {'A': ['B', 'C'],
         'B': ['C', 'D'],
         'C': ['D'],
         'D': ['C'],
         'E': ['F'],
         'F': ['C']
         }

#新的图形搜索对象的初始化
graph1 = GraphSearch(graph)

print(graph1.find_path('A', 'D'))
print(graph1.find_all_path('A', 'D'))
print(graph1.find_shortest_path('A', 'D'))