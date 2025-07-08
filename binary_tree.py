class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if(self.data == data):
            return
        
        if(data < self.data):
            # add data to the left
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinaryTreeNode(data)

        else:
            # add data to the right
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinaryTreeNode(data)

    def inOrderTraversal(self):
        elements = []

        if self.left:
            elements += self.left.inOrderTraversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.inOrderTraversal()

        return elements
    
def build_tree(elements):
    root = BinaryTreeNode(elements[0])

    for i in range(len(elements)):
        root.add_child(elements[i])

    return root
    
if __name__ == '__main__':
    numbers = [45,23,67,89,54,2,6,8,34,56]

    n_tree = build_tree(numbers)
    print(n_tree.inOrderTraversal())
