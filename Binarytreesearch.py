class Node:
    def __init__(self,key=None):
        self.key = key
        self.left = None
        self.right = None
        
# function for the create binary tree

def insertele(root,data):
    if root is None:
        return Node(data)
    elif root.key < data:
        root.right = insertele(root.right,data)
    else:
        root.left = insertele(root.left,data)
        
    return root
# function of the minimumnode of the binary search tree
    
def minimumnode(root):
    if root is None:
        return
    else:
        current  = root
        while current.left is not None:
            current = current.left
            
    return current.key
# function of the maximumnode of the binary search tree
    
def maximumnode(root):
    if root is None:
        return
    else:
        current = root
        while current.right is not None:
            current = current.right
            
    return current.key
    
# function of the no of the nodes in binary  search tree
    
def noofnode(root):
    if root is None:
        return 0
    else:
        return noofnode(root.left)+noofnode(root.right)+1
        
# function of the common node of the two different elements

def leastcommonnode(root,n1,n2):
    if root is None:
        return
    elif root.key < n1 and root.key <n2:
        leastcommonnode(root.left,n1,n2)
    else:
        leastcommonnode(root.right,n1,n2)
    return root.key
     
# function of the displaying elements of the binary search tree       
def dispalyele(root):
    # displaying inorder
    if root is None:
        return 
    else:
        dispalyele(root.left)
        print(root.key,end=" ")
        dispalyele(root.right)
    
    """
    # dispalying preorder
    
    if root:
        print(root.key,end=" ")
        dispalyele(root.left)
        dispalyele(root.right)
    # dispalying postorder    
    if root:
        dispalyele(root.left)
        dispalyele(root.right)
        print(root.key,end=" ")
    """
    
    
    
        
root = None
root = insertele(root,50)
root = insertele(root,10)
root = insertele(root,100)
root = insertele(root,150)
root = insertele(root,5)
root = insertele(root,-5)
print(minimumnode(root))
print(maximumnode(root))
print(noofnode(root))
print(leastcommonnode(root,-5,5))
dispalyele(root)
        
    
