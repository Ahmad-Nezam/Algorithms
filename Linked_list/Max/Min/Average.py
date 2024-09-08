# max 
class SList:
    def __init__(self):
        self.items = []

    def add(self, value):
        self.items.append(value)

    def max(self):
        if not self.items:
            return None  
        max_value = self.items[0]  
        for item in self.items:
            if item > max_value:
                max_value = item  
        return max_value

slist = SList()
slist.add(10)
slist.add(15)
slist.add(50)
slist.add(60)

print(slist.max())  

# min
class SList:
    def __init__(self):
        self.items = []

    def add(self, value):
        self.items.append(value)

    def min(self):
        if not self.items:
            return None  
        min_value = self.items[0]  
        for item in self.items:
            if item < min_value:
                min_value = item  
        return min_value

slist = SList()
slist.add(10)
slist.add(15)
slist.add(50)
slist.add(60)

print(slist.min())  


# Avg

class SList:
    def __init__(self):
        self.items = []

    def add(self, value):
        self.items.append(value)

    def average(self):
        if not self.items:
            return None  
        total_sum = sum(self.items) 
        count = len(self.items)  
        return total_sum / count 


slist = SList()
slist.add(10)
slist.add(20)
slist.add(30)
slist.add(40)

print(slist.average()) 
