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

    
    def search_tree(self, val):
        if self.data == val:
            return True
        
        elif val < self.data:
            if self.left:
                return self.left.search_tree(val)
            else:
                return False
            
        elif val > self.data:
            if self.right:
                return self.right.search_tree(val)
            else:
                return False
    
    def find_min(self):
        if self.left:
            return self.left.find_min()
        else:
            return self.data
        
    def find_max(self):
        if self.right:
            return self.right.find_max()
        else:
            return self.data
        
    def calculate_sum(self):
        
        sum = self.data

        if self.left:
            sum += self.left.calculate_sum()

        if self.right:
            sum += self.right.calculate_sum()
        
        return sum

            # if self.left:
    def inOrderTraversal(self):
        elements = []

        if self.left:
            elements += self.left.inOrderTraversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.inOrderTraversal()

        return elements

    def preorder_traversal(self):
        elements = [self.data]

        if self.left:
            elements += self.left.preorder_traversal()
        
        if self.right:
            elements += self.right.preorder_traversal()
        
        return elements
    
    def postorder_traversal(self):
        elements = []

        if self.left:
            elements += self.left.postorder_traversal()
        
        if self.right:
            elements += self.right.postorder_traversal()

        elements.append(self.data)
        
        return elements
    
    def delete(self, val):

        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.right is None and self.left is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            
            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)

        return self

def build_tree(elements):
    root = BinaryTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root
    
if __name__ == '__main__':
    numbers = [17,4,1,20,9,23,18,24]

    a1 = a2 = a3 = [], [], []

    root = build_tree(numbers)
    a1 = root.inOrderTraversal()
    a2 = root.preorder_traversal()
    a3 = root.postorder_traversal()
    print(a1,a2,a3)

    root.delete(20)

    print(root.inOrderTraversal())

    sum = root.calculate_sum()
    print(sum)


