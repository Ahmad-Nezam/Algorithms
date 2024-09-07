# Add Front
class Node: 
    def __init__(self , new_data):
        self.data = new_data
        self.next = None
def insert_front(head , new_data):
    new_node = Node(new_data)
    new_node.next = head
    return new_node
def print_list(head):
    cuur = head
    while cuur is not None:
        print(f"{cuur.data}" , end='')
        cuur = cuur.next
    print()
def delete_head(head):
  
   
    if head is None:
        return None

    
    temp = head

  
    head = head.next

   
    del temp

    return head


if __name__ == "__main__":
    
    head = Node(2)
    head.next = Node(3)
    head.next.next = Node(4)
    head.next.next.next = Node(5)

    head = delete_head(head)
    print_list(head)
    print("Original Linked List:", end="")
    print_list(head)

   
    print("After inserting Nodes at the front:", end="")
    data = 1
    head = insert_front(head, data)

   
    print_list(head)

