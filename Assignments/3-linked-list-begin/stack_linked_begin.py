from linkedlist_begin import LinkedList

class LinkedStack:
    def __init__(self):
        """Use a LinkedList to store the stack items"""
        self.items = LinkedList()
                 
    def pop(self):
        """TODO: Implement push"""
        last = self.items.last
        self.items.__delitem__(self.items.numItems-1)
        return last.getItem()
    
    def push(self,item):
        """TODO: Implement pop"""
        self.items.append(item)

    def top(self):
        """TODO: Implement top"""
        return self.items.last.getItem()

    def isEmpty(self):
        """TODO: Implement isEmpty"""
        return self.items.numItems == 0

    def clear(self):
        """TODO: Implement clear"""
        self.items = LinkedList()
