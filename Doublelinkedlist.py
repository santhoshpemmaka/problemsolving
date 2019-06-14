#code
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
class Linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def insert(self,data):
        new_node = Node(data)
        
        if self.head == None and self.tail == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            
    def display(self):
        if self.head == None:
            return 
        else:
            temp = self.head
            while temp:
                print(temp.data,end=" ")
                temp = temp.next
            print()
            temp1= self.tail
            while temp1:
                print(temp1.data,end=" ")
                temp1 = temp1.prev
                
l = Linkedlist()
l.insert(10)
l.insert(1)
l.insert(5)           
l.insert(20)       
l.insert(25)
l.insert(30)
l.display()
        
        
