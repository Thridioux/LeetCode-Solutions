class Node():
    def __init__(self, data):
        self.data = data
        self.ref = None     # we could use next instead of ref

class LinkedList():
    def __init__(self):
        self.head = None

    def print_LL(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data, "-->", end=" ")
                n = n.ref
                
            
    def add_begin(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

    def add_after(self, data, x): # x is the data after which we want to add the new node
        n = self.head
        while n is not None:
            if x == n.data:
                break
            n = n.ref
        if n is None:
            print("Node is not present in LL")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
    
    def add_before(self,data,x):  
        if self.head is None:
            print("Linked List is empty")
            return
        
        if self.head == x:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return
        
        n = self.head
        while n.ref is not None: # if the node is not the last node
            if n.ref.data == x:
                break
            n = n.ref # move to the next node
        
        if n.ref is None:
            print("Node is not FOUND in LL")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node


    def insert_empty(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("Linked List is not empty")


    def delete_begin(self):
        if self.head is None:
            print("Linked List is empty,so we can't delete node")
        else:
            self.head = self.head.ref # move the head to the next node
    
    def delete_end(self):
        if self.head is None:
            print("Linked List is empty,so we can't delete node")
        elif self.head.ref is None: # if there is only one node
            self.head = None
        else:
            n = self.head
            while n.ref.ref is not None: # if the next node is not the last node
                n = n.ref
            n.ref = None

    def delete_by_value(self, x):
        if self.head is None:
            print("Linked List is empty,so we can't delete node")
            return
        if x == self.head.data: # if the node to be deleted is the first node
            self.head = self.head.ref # move the head to the next node
            return
        n = self.head
        while n.ref is not None: # if the node to be deleted is not the last node
            if x == n.ref.data: # if the next node is the node to be deleted
                break
            n = n.ref
        if n.ref is None: # if the node to be deleted is not present in the LL
            print("Node is not present in LL")
        else:
            n.ref = n.ref.ref 
       


LL1 = LinkedList()
LL1.add_begin(10)
LL1.add_begin(20)
LL1.add_begin(30)
LL1.delete_by_value(10)
LL1.print_LL() # 30 --> 20 -->
      





    
        
# LL1 = LinkedList()
# LL1.add_begin(10)
# LL1.delete_end()
# LL1.print_LL() 
       


# LL1 = LinkedList()
# LL1.insert_empty(10)
# LL1.print_LL() # 10 -->


# LL1 = LinkedList()
# LL1.add_begin(10)
# LL1.add_begin(20)
# LL1.add_end(30)
# LL1.add_after(15, 20)
# LL1.print_LL() # 20 --> 15 --> 10 --> 30 -->


# LL1 = LinkedList()
# LL1.add_begin(10)
# LL1.add_begin(20)
# LL1.add_end(30)
# LL1.add_before(15, 10)
# LL1.print_LL() # 20 --> 15 --> 10 --> 30 -->



