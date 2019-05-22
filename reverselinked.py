def reverseList(self):
    # Code here
    if self.head is None:
        return None
    else:
        prev = None
        current = self.head
        while current != None:
            next1 = current.next
            current.next = prev
            prev = current
            current = next1
        self.head= prev
        
