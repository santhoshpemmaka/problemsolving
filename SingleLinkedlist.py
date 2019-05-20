class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def insertele(self,data):
        
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            
        else:
            last = self.head
            while last.next != None:
                last = last.next
            
            last.next = new_node
    def insertafterele(self,prevnode,data):
        
        new_node = Node(data)
        if prevnode == None:
            return
        else:
            new_node.next = prevnode.next
            prevnode.next = new_node
            
            
    def deletenode(self,node):
        
        if node == self.head:
            self.head = self.head.next
            
        else:
            node.next = node.next.next
            
    def count(self):
        counter =0
        last = self.head
        while last:
            last = last.next
            counter = counter+1
        return counter
        
    def middlenode(self):
        if self.head == None:
            return
        else:
            curr = self.head
            prev = self.head
        # linked list no of nodes will be odd curr.next.next != None and no of nodes will even curr.next != None
            while curr.next.next != None and prev.next != None:
                prev = prev.next
                curr = curr.next.next
            return prev.data
            
            
    def display(self):
        if self.head == None:
            return
        else:
            last = self.head
            
            while last:
                print(last.data)
                last = last.next

llist = LinkedList()
llist.insertele(50)
llist.insertele(25)
llist.insertele(10)
llist.insertele(0)
llist.insertele(5)
#llist.insertafterele(llist.head.next,1)
#llist.deletenode(llist.head.next)
#print(llist.count())
llist.display()
print('The middle element',llist.middlenode())
