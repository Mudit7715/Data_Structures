class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head == None:
            print('Linked List is Empty')
            return
        
        itr = self.head
        llstr = ''

        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next
        print(llstr)

    def get_length(self):
        itr = self.head
        count = 0

        while itr:
            count += 1
            itr = itr.next

        return count

    def append_at_first(self, data):

        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        node = Node(data, None)

        if self.head == None:
            self.head = node
            return 

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = node

    def insert_at_index(self, data, index):
        count = 0

        if index<0 or index> self.get_length():
            print("Invalid index")
            return

        if index == 0:
            self.append_at_first(data)
            return

        itr = self.head

        while itr:
            if count == index-1:
                node= Node(data, itr.next)
                itr.next = node
                # node.next = itr.next.next
                break
            itr = itr.next
            count +=1

    
    def remove_at_index(self, index):
        count = 0

        if index <0 or index > self.get_length():
            print("Invalid Index")
            return 

        itr = self.head
        while itr:
            if count == index-1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count +=1

    def insert_list(self , dataList):

        self.head = None

        for data in dataList:
            self.insert_at_end(data)

    def insert_after_values(self, data_after, data_to_insert):
        
        itr = self.head

        while itr:
            if(itr.data == data_after):
                itr.next = Node(data_to_insert, itr.next)
                return
            # else:
            #     print("Provided data index does not exist in the linkedList")
            #     return
            itr = itr.next
        print("Provided data index does not exist in the linkedList")

    def remove_by_value(self, value):
        if self.head and self.head.data == value:
            self.head = self.head.next
            return  
        
        itr = self.head

        while itr and itr.next:
            if(itr.next.data == value):
                itr.next = itr.next.next
                return
            itr = itr.next
        print("value not found")



if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_list(["banana","mango","grapes","orange"])
    ll.print()
    ll.insert_after_values("mango","apple") # insert apple after mango
    ll.print()
    ll.remove_by_value("orange") # remove orange from linked list
    ll.print()
    ll.remove_by_value("figs")
    ll.print()
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    ll.print()               
