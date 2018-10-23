import BinarySearchTree
import math

class RBNode(BinarySearchTree.Node):
    def __init__(self,key,value):
        BinarySearchTree.Node.__init__(self,key,value)
        self.isRed=True
    def isRed(self):
        return self.isRed
    def setIsRed(self,isRed):
        self.isRed=isRed
    def __repr__(self):
        return "Node{ key : " + str(self.key) + ", value : " + str(self.value) + ", isRed:"+str(self.isRed)+"}"







    def size(self):
        size=1
        if(self.left!=None):
            size+=self.left.size()
        if(self.right!=None):
            size+=self.right.size()
        return size
    def verifyBlackHeight(self,height):
        if(not self.isRed):
            height-=1;
        if(self.right==None and height!=0):
            return False
        if(self.left==None and height!=0):
            return False
        if(self.right!=None and self.right.verifyBlackHeight(height)==False):
            return False
        if(self.left!=None and self.left.verifyBlackHeight(height)==False):
            return False


        return True



class RedBlackBST(BinarySearchTree.BST):
    def __init__(self):
        BinarySearchTree.BST.__init__(self)
    def __repr__(self):
        return self.printPart(self.root)

    def printPart(self,node):
        if(node==None):
             return "X"

        leftString=self.printPart(node.left)
        rightString=self.printPart(node.right)


        sideWidth=max(len(leftString.split("\n")[0]),len(rightString.split("\n")[0]))
        width=sideWidth+len(str(node.key))+sideWidth
        halfWidth=math.floor(sideWidth/2)

        string=halfWidth*" "+"/"+(sideWidth-halfWidth-1)*"-"+str(node.key)+(sideWidth-halfWidth-1)*"-"+"\\"+halfWidth*" "+"\n"

        leftArr=leftString.split('\n')
        rightArr=rightString.split("\n")
        for i in range(0,max(len(leftArr),len(rightArr))):
            if(len(leftArr)>i):
                smallSideWidth=math.floor((sideWidth-len(leftArr[i]))/2)
                string+=smallSideWidth*" "
                string+=leftArr[i]
                string+=(sideWidth-len(leftArr[i])-smallSideWidth)*" "
            else:
                string+=" "*(sideWidth)

            string+=(width-sideWidth*2)*" "

            if(len(rightArr)>i):
                smallSideWidth=math.floor((sideWidth-len(rightArr[i]))/2)
                string+=smallSideWidth*" "
                string+=rightArr[i]
                string+=(sideWidth-len(rightArr[i])-smallSideWidth)*" "
            else:
                string+=" "*(sideWidth)
            string+="\n"

        return string[:-1]


    def put(self, keyIn, valueIn):
        if self.root.getKey() == None:
            self.root = RBNode(keyIn, valueIn)
        else:
            self.root = self.__put(self.root, keyIn, valueIn)
    def __put(self, nodeIn, keyIn, valueIn):
        if nodeIn == None or nodeIn.getKey() == None:
            return RBNode(keyIn, valueIn)
        else:
            if keyIn > nodeIn.getKey():
                nodeIn.setRight(self.__put(nodeIn.getRight(), keyIn, valueIn))
            else:
                nodeIn.setLeft(self.__put(nodeIn.getLeft(), keyIn, valueIn))
            return nodeIn
    def getBlackHeight(self):#assumes tree is properly made
        node=self.root
        blacks=1
        while(node.left!=None):
            node=node.left
            if not node.isRed:
                blacks+=1
        return blacks
def isGParent(node):
    if(node.left!=None and (node.left.right!=None or node.left.left!=None)) or (node.right!=None and (node.right.left!=None or node.right.right!=None)):
        return True;
    return False
def isRBBST(tree):
    if(tree.root.isRed):
        return False
    if(tree.root.verifyBlackHeight(tree.getBlackHeight()) == False):
        return False
    return isRBBSTPart(tree.root)
def isRBBSTPart(node):
    if(node.isRed):
        if((node.left!=None and node.left.isRed) or (node.right!=None and node.right.isRed)):
            return False
    if(node.left!=None and not isRBBSTPart(node.left)):
        return False
    if(node.right!=None and not isRBBSTPart(node.right)):
        return False
    return True


def rotateRight(node):
    if(node.left==None):
        return None
    newNode=node.left
    node.left=newNode.right
    newNode.right=node
    return newNode
def rotateLeft(node):
    if(node.right==None):
        return None
    newNode=node.right
    node.right=newNode.left
    newNode.left=node
    return newNode

x = RedBlackBST()
x.put(10,1)
x.put(5,2)
x.put(15,3)
x.put(4,4)
x.put(6,5)
x.put(14,6)
x.put(16,7)
print(str(x)+"\n\n\n")
x.root=rotateRight(x.root)
print(str(x)+"\n\n\n")
x.root.right=rotateLeft(x.root.right)
print(str(x)+"\n\n\n")

print(isGParent(x.root))
print(isGParent(x.root.right))
print(isGParent(x.root.right.right))


#Make the tree from the website
y=RedBlackBST()
y.put(7,1)
y.put(3,1)
y.put(18,1)
y.put(10,1)
y.put(22,1)
y.put(8,1)
y.put(11,1)
y.put(26,1)
print(y)
print(isRBBST(y))
y.root.isRed=False
y.root.left.isRed=False
y.root.right.left.isRed=False
y.root.right.right.isRed=False
print(isRBBST(y))
y.root.right.isRed=False
print(isRBBST(y))
