class Node: #defining node of linked list                              
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
    
class LinkedList:  #initializing linked list

    def __init__(self):
        self.head=None #no elements when starting
        
    def insert_at_beginning(self,data): #adding new node at beginning of linked list
        node=Node(data,self.head)
        self.head=node
        
    def insert_at_end(self,data):
        if self.head is None:
           node=Node(self.data,None)
        else:
            i=self.head
            while i.next:
                i=i.next
            i.next= Node(data,None)
            
    def insert_values(self,data_list):
        for data in data_list:
           self.insert_at_end(data) 
           
    def get_length(self):
        i=self.head
        count=0
        while i:
            count+=1
            i=i.next
        return count
        
    def remove_at_index(self,index):
        if index<0 or index>=self.get_length():
            print("invalid index")
        elif index==0:
            self.head=self.head.next
        else:
            i=self.head
            count=0
            while i:
                if count==index-1:
                    i.next=i.next.next
                    break
                count+=1
                i=i.next
                
    def insert_at_index(self,data,index):
        if index<0 or index>self.get_length():
            print("invalid index")
        elif index==0:
            node=Node(data,head)
            self.head=node
        else:
            i=self.head
            count=0
            while i:
                if count==index-1:
                    node=Node(data,i.next)
                    i.next=node
                    break
                count+=1
                i=i.next
                            
    def print(self):
        if self.head is None:
            print("linked list is empty")
        else:
            i=self.head
            while i:
                print(i.data)
                i=i.next
                
l=LinkedList() #initializing linked list
l.insert_at_beginning(5) # accessing methods of class LinkedList and adding elemnts in the starting
l.insert_at_beginning(23)
l.insert_at_beginning(46)
l.insert_at_end(24)
l.insert_at_beginning(203)
l.insert_values(["ch","sk"])
l.remove_at_index(1)
l.remove_at_index(20)
l.insert_at_index(20,3)
l.print()
print("legth of linked list is",l.get_length())

l2=LinkedList()
l2.print()
        
