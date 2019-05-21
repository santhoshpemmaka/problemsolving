class Node:
    def __init__(self,key=None):
        self.key = key
        self.right = None
        self.left = None

# function implemented array to binary search tree
        
def arraytoBST(arr):
    
    if len(arr)==0:
        return None
    
    mid = len(arr)//2;
    
    root = Node(arr[mid])
    
    root.left = arraytoBST(arr[:mid])
    root.right = arraytoBST(arr[mid+1:])
    return root
    
# function implemented binary search tree to array
arr=[]
def BST_to_array(root):

    if root is None:
        return 
    else:
        BST_to_array(root.left)
        arr.append(root.key)
        BST_to_array(root.right)
    return arr
# Displaying binary search tree elements  

# function implemented mirror of the binary search tree

def mirror_binary_tree(root):
    if root is None:
        return 
    else:
        temp = root
        
        mirror_binary_tree(root.left)
        mirror_binary_tree(root.right)
    
        temp = root.left
        root.left = root.right
        root.right= temp
    
def preorder(root):
    if root:
        print(root.key,end=" ")
        preorder(root.left)
        preorder(root.right)
    
        
root = arraytoBST([1,2,3,4,5,6,7])
print(BST_to_array(root))
preorder(root)
print()
mirror_binary_tree(root)
preorder(root)


