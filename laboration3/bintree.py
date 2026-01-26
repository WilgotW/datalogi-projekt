class Bintree:
    def __init__(self):
        self.root = None
        self.size = 0

    def __contains__(self, item):
        if item in self.root:
            return True
        return False
    
    def store(self, item):
        self.root = rekstore(item)

    def write(self):
        re

    def recstore(self, item):
        return
    
    def recsearch(self):
        return
    
    def recwrite(self):
        return
    
class TreeNode:
    def __init__(self, key, payload, left=None, right=None, parent=None):
        self.key = key
        self.payload = payload
        self.left_child = left
        self.right_child = right
        self.parent:TreeNode = parent

    def hasLeftChild(self):
        return self.left_child != None
    
    def hasRightChild(self):
        return self.right_child != None
    
    def isLeftChild(self):
        return self.parent & self.parent.left_child == self
    
    def isRightChild(self):
        return self.parent & self.parent.hasRightChild== self
    
    def isRoot(self):
        return self.parent == None
    
    def isLeaf(self):
        return self.right_child == None & self.left_child == None
    
    def hasChildren(self):
        return self.right_child | self.left_child