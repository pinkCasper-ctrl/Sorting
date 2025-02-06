class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
class BST:
    def __init__(self):
        self.root = None
        
    def create(self, value):
        newNode = Node(value)
        
        if not self.root:
            self.root = newNode
        else:
            self.insertNode(self.root, newNode)
        
    def insertNode(self, currentNode, node):
        if node.value < currentNode.value:
            if currentNode.left is None:
                currentNode.left = node
            else:
                self.insertNode(currentNode.left, node)
        else:
            if currentNode.right is None:
                currentNode.right = node
            else:
                self.insertNode(currentNode.right, node)
    
    # Treeyi daha anlaşılır yazdırabilmek için __str__ metodunu ekliyoruz
    def __str__(self):
        values = []
        self.inOrderTraversal(self.root, values)
        return ' '.join(str(value) for value in values)

    def inOrderTraversal(self, node, values):
        if node:
            self.inOrderTraversal(node.left, values)
            values.append(node.value)
            self.inOrderTraversal(node.right, values)
    
# Ağaç oluşturma ve değer ekleme
tree = BST()
tree.create(10)
tree.create(21)
tree.create(5)
tree.create(32)
tree.create(32)
tree.create(-1)

# Ağaç yazdırma
print(tree)
