
class Node(object):
    def __init__(self, data=None, previous=None, next=None):
        self.data = data
        self.previous = previous
        self.next = next

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, data):
        self.data = data

    def set_next(self, next):
        self.next = next


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, data):
        new_node = Node(data)
        cur_node = self.head
        if cur_node == None:
            self.head = new_node
            return

        while cur_node.get_next() != None:
            cur_node = cur_node.get_next()
        cur_node.set_next(new_node)

    def unshift(self, data):
        new_node = Node(data)
        first_node = self.head
        new_node.set_next(first_node)
        self.head = new_node

    def shift(self):
        cur_node = self.head
        self.head = cur_node.get_next()

    def pop(self):
        cur_node = self.head
        while cur_node.get_next().get_next() != None:
            cur_node = cur_node.get_next()
        cur_node.set_next(None)

    def show(self):
        cur_node = self.head
        output = ""
        while cur_node != None:
            output += str(cur_node.get_data()) + "---->"
            cur_node = cur_node.get_next()
        print(output)

my_list = LinkedList()
my_list.push(10)
my_list.push(100)
my_list.push(1000)
my_list.push(10000)
my_list.push(100000)
my_list.show()

my_list.pop()
my_list.show()

my_list.shift()
my_list.show()

my_list.unshift(11111)
my_list.show()