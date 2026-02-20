
class TreeNode: 
    def __init__(self, key = None):
        self.key = key
        self.parent = None
        self.right_node = None
        self.left_node = None


class Bintree: 
    def __init__(self):
        self.root:TreeNode = None
        self.key = None

    def store(self, key):
        #sort new key into tree
        if self.root is None:
            self.root = TreeNode(key)
        else:
            recstore(self.root, key)
    
    def __contains__(self, key):
        #return true if key is found in the tree
        if self.root is None:
            return False
        elif key == self.root.key:
            return True
        else:
            return recsearch(self.root, key)
    
    def write(self):
        #print tree in inorder
        ordered_list = []
        recwrite(self.root, ordered_list)
        print(ordered_list)



#recursive store
def recstore(current_node:TreeNode, key):
    #create new node at right place
    #recrusive function to find right place to store key 
    #go left
    if key <= current_node.key:
        if current_node.left_node is None:
            new_node = TreeNode(key)
            new_node.parent = current_node
            current_node.left_node = new_node
        else:
            #keep going down
            recstore(current_node.left_node, key)
    #go right
    if key > current_node.key:
        if current_node.right_node is None: 
            new_node = TreeNode(key)
            new_node.parent = current_node
            current_node.right_node = new_node
        else:
            recstore(current_node.right_node, key)    

def recsearch(current_node:TreeNode, key):
    if key == current_node.key:
        return True

    if key <= current_node.key and current_node.left_node is not None:
        return recsearch(current_node.left_node, key)
    elif key > current_node.key and current_node.right_node is not None:
        return recsearch(current_node.right_node, key)
    else:
        return False

def recwrite(current_node:TreeNode, ordered_list:list):
    if current_node is None:
        return
    
    recwrite(current_node.left_node, ordered_list)
    ordered_list.append(current_node.key)
    recwrite(current_node.right_node, ordered_list)
    