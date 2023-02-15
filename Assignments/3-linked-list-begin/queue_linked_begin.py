from linkedlist_begin import LinkedList

class LinkedQueue:
    def __init__(self):
        """Use a LinkedList to store the queue items"""
        self.items = LinkedList()
                 
    def dequeue(self):
        """TODO: Implement dequeue"""
        first = self.front()
        del self.items[0]
        return first
    
    def enqueue(self,item):
        """TODO: Implement enqueue"""
        self.items.append(item)

    def front(self):
        """TODO: Implement front"""
        return self.items.first.getNext().getItem()

    def isEmpty(self):
        """TODO: Implement isEmpty"""
        return self.items.numItems == 0

    def clear(self):
        """TODO: Implement clear"""
        self.items = LinkedList()
