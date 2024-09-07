class Node:
    def __init__(self , data = None , next= None):
        self.data = data
        self.next = next
class linkedlist:
    def __init__(self):
        self.head = None

    def insert_at_begin(self , data):
        node = Node(data , self.head)
        self.head = node

    def print(self):
        if self.head == None:
            print('linked list is empty')
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next 
        print(llstr) 

    def insert_at_end(self , data):
        if self.head is None:
            self.head = Node(data , None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data , None)

    def insert_values(self , data_list):
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count
    
    def remove_at(self,index):
        if index < 0 or index >= self.get_length():
            raise Exception('invalid index')
        if index == 0:
            self.head = self.head.next
            return
        
        count = 0 
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break 
            itr = itr.next
            count += 1
    
    def insert_at(self , index , data):
        if index < 0 or index >= self.get_length():
            raise Exception('invalid index')
        if index == 0 :
            self.insert_at_begin(data)
            return
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                node = Node(data,itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1




if __name__ == '__main__':
    ll = linkedlist()
    ll.insert_at_begin(5)
    ll.insert_at_begin(6)
    ll.insert_at_begin(7)
    ll.insert_at_begin(8)
    ll.insert_at_begin(9)
    ll.insert_at_end(20)
    ll.insert_at_end(21)
    ll.insert_at_begin(10)
    ll.insert_values(['apple','banna','mango'])
    print('the length of the list is : ',ll.get_length()) 
    ll.insert_at(4,'ahmad')
    ll.print()
    ll.remove_at(4)
    ll.print()
 