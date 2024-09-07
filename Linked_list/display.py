
class Node:
    def __init__(self, value):
        self.value = value 
        self.next = None   


class SLL:
    def __init__(self):
        self.head = None 

   
    def add(self, value):
        new_node = Node(value)
        if not self.head:  
            self.head = new_node
        else:
            runner = self.head
            while runner.next:  
                runner = runner.next
            runner.next = new_node 

 
    def display(self):
        if not self.head:
            return "List is empty"  

        runner = self.head
        result = []  

        while runner:
            result.append(str(runner.value))  
            runner = runner.next 

        return " -> ".join(result)  

my_list = SLL()
my_list.add(10)
my_list.add(20)
my_list.add(30)
my_list.add(40)


print(my_list.display())
