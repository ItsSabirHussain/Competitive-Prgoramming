class Node:
    def __init__(self, name):
        self.name = name
        self.childrens = []
        self.leefanddepth = {}

    def addChildren(self, name):
        self.childrens.append(Node(name))

    def depthFirstSearch(self, array):
        array.append(self.name)
        for child in self.childrens:
            child.depthFirstSearch(array)
        return array


if __name__ == '__main__':
    root = Node("A")
    root.addChildren("B")
    root.addChildren("C")
    root.childrens[0].addChildren("D")
    root.childrens[1].addChildren("E")
    print(root.depthFirstSearch([]))
