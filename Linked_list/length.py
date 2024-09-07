class Node:
    def __init__(self , data = None , next= None):
        self.data = data
        self.next = next
class linkedlist:
    def __init__(self):
        self.head = None

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count 
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

if __name__ == '__main__':
    ll = linkedlist()
    ll.insert_at_end(20)
    ll.insert_at_end(21)
    print('the length of the list is : ',ll.get_length()) 