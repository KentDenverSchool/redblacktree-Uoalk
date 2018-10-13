import BinarySearchTree

class RBNode(BinarySearchTree.Node):
    def __init__(self,key,value,isRed):
        BinarySearchTree.Node(key,value)
        self.isRed=isRed
    def isRed(self):
        return self.isRed
    def __repr__(self):
        return "Node{ key : " + str(self.key) + ", value : " + str(self.value) + ", isRed:"+str(self.isRed)+"}"

class RedBlackBST(BinarySearchTree.BST):
    def __init__(self):
        BinarySearchTree.BST.__init__(self)



x = RedBlackBST()
print(x)
