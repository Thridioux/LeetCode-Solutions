class Node():
    def __init__(self,data):
        self.data = data
        self.nref = None
        self.pref = None


class DoublyLinkedList():   
    def __init__(self):
        self.head = None

    def print_LL(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data, "-->", end=" ")
                n = n.nref
            print()
    
    def print_LL_reverse(self): 
        if self.head is None:
            print("Linked List is empty")
        else:
            n = self.tail
            while n is not None:
                print(n.data, "-->", end=" ")
                n = n.pref
            print()
    
    def add_begin(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node    
        else:
            new_node.nref = self.head
            self.head.pref = new_node
            self.head = new_node

    def insert_empty(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
            self.tail = new_node # the only node in the LL
        else:
            print("Linked List is not empty")

    def add_begin(self,data):
        new_node = Node(data)
        if self.head is None: # if the LL is empty
            self.head = new_node # the new node is the head
            self.tail = new_node # the new node is the tail
        else:
            new_node.nref = self.head  # the new node's next reference is the current head
            self.head.pref = new_node
            self.head = new_node

    def add_end(self,data):
        new_node = Node(data)
        if self.head is None: # if the LL is empty
            self.head = new_node
            self.tail = new_node
        else:
            n = self.head
            while n.nref is not None: # if the node is not the last node
                n = n.nref # move to the next node
            n.nref = new_node # the last node's next reference is the new node
            new_node.pref = n
            self.tail = new_node # the new node is the tail

    def add_after(self,data,x):
        if self.head is None:
            print('Linked List is empty')
        else:
            n = self.head
            while n is not None:
                if x == n.data:
                    break
                n = n.nref
            if n is None:
                print('Node is not present in the LL')  
            else:
                new_node = Node(data)
                new_node.pref = n 
                new_node.nref = n.nref
                if n.nref is not None: # if the node is not the last node
                    n.nref.pref = new_node # the next node's previous reference is the new node
                n.nref = new_node # the current node's next reference is the new node

                
    def add_before(self,data,x):
        if self.head is None:
            print('Linked List is empty')
        else:
            n = self.head
            while n is not None:
                if x == n.data:
                    break
                n = n.nref
            if n is None:
                print('Node is not present in the LL')
            else:
                new_node = Node(data)
                new_node.nref = n
                new_node.pref = n.pref
                if n.pref is not None: # if the node is not the first node
                    n.pref.nref = new_node  # the previous node's next reference is the new node
                else:
                    self.head = new_node # the new node is the head
                n.pref = new_node # the current node's previous reference is the new node

    def delete_begin(self):
        if self.head is None: # if the LL is empty
            print("Linked List is empty")
        elif self.head.nref is None: # if the LL has only one node
            self.head = None 
        else:
            self.head = self.head.nref # the next node is the head
            self.head.pref = None # the head's previous reference is None

    def delete_end(self):
        if self.head is None: # if the LL is empty
            print("Linked List is empty")
            return 
        if self.head.nref is None: # if the LL has only one node
            self.head = None
            print("DLL is empty after deleting the node")
        else:
            n = self.head
            while n.nref is not None: # if the node is not the last node we will achieve the last node at the end
                n = n.nref
            n.pref.nref = None 

    def delete_by_value(self,x):
        if self.head is None:
            print('Linked List is empty')
            return
        if self.head.nref is None: # if the linked List has only one mode
            if x == self.head.data:
                self.head = None
            else:
                print('x is not present in the LL')
            return
            
        
        if self.head.data == x: # if the node to be deleted is the first node
            self.head = self.head.nref
            self.head.pref = None

        else:  # if the node to be deleted is not the first node itself
            n = self.head
            while n.nref is not None: 
                if x == n.data:
                    break
                n = n.nref
                if n.nref is not None: # if the node is not the last node 
                    n.pref.nref = n.nref
                    n.nref.pref = n.pref
                else: # if the node is the last node !!! n is pointing the last node now
                    if n.data == x:
                        n.pref.nref = None
                    else:
                        print('x is not present in the LL')
                        return
    



                    


                







dll2 = DoublyLinkedList()
dll2.add_begin(10)
dll2.add_begin(20)
dll2.add_begin(30)
dll2.add_begin(40)
dll2.print_LL() 
dll2.delete_by_value(20)
dll2.print_LL() # 40 --> 30 --> 10 -->









        
# dll1 = DoublyLinkedList()   
# dll1.add_begin(10)
# dll1.add_before(20,10)
# dll1.print_LL() # 20 --> 10 -->

# dll2 = DoublyLinkedList()
# dll2.add_begin(10)
# dll2.add_after(20,10)
# dll2.add_before(30,20)
# dll2.print_LL() # 10--> 20 -->


# dll2 = DoublyLinkedList()
# dll2.add_begin(10)
# dll2.add_after(20,10)
# dll2.add_before(30,20)
# dll2.print_LL() # 10--> 30 --> 20 -->
# dll2.delete_end()
# dll2.print_LL() # 10--> 30 --> 



# dll2 = DoublyLinkedList()
# dll2.add_begin(10)
# dll2.delete_end()

# Linked List is empty why did it not print "DLL is empty after deleting the node"?











   

    
    



                






    












        



















    

        

       




                    




    

















