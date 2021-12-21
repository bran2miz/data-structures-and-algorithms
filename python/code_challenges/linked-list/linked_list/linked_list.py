class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    # ll head of 1
    # [1] -> [2] -> None
    # insert 3
    # ll know the head 3
    # [3] -> [1] -> [2] -> None

    def insert(self, value):
        try:
            node = Node(value) # Node of [3]
            if self.head is not None:
                node.next = self.head
            self.head = node
        except Exception as e:
            print(f'There was an unexpected error {e}')

    def includes(self, value):
        try:
            include = False
            if self.head is None:
                include = False
            else:
                current = self.head
            while current is not None:
                if current.value == value:
                    include = True
                current = current.next
            return include
        except Exception as e:
            print(f'There was an unexpected error {e}')

    def to_string(self):
        try:
            linked_list_output = ""
            if self.head is None:
                linked_list_output = '{NONE}'
            else:
                linked_list_output += '{}{}{}'.format('{ ',self.head.value,' }')
                current = self.head
                while current.next:
                    linked_list_output += ' -> {}{}{}'.format('{ ',current.next.value,' }')
                    current = current.next

                linked_list_output += f' -> NONE'
                return linked_list_output
        except Exception as e:
             print(f'There was an unexpected error {e}')

    def append(self, num):
        """
        linked list function called append to append a file in the end of the linked list
        """
        newNode = Node(num)
        current = self.head
        if current:
            while current.next != None:
                current = current.next
            current.next = newNode
        else:
            self.head = Node(num)

    def insert_before(self, target, num):
        """
        class method to insert a number before targeted value
        """
        newNode = Node(num)
        current = self.head
        if current == None:
            newNode = Node.insert(num)
        else:
            found = False
            while current:
                if current.next == None:
                    break
                if current.next.data == target:
                    found = True
                    newNode.next = current.next
                    current.next = newNode
                    break
                else:
                    current = current.next
            if found != True:
                print(f"Your target node of was not found in the list!")

    def insert_after(self, target, num):
        """
        class method to insert a number after targeted value
        """
        newNode = Node(num)
        current = self.head
        temp = self.head
        while current.next != None:
            if current.data == target:
                temp = temp.next
                current.next = newNode
                current = current.next
                current.next = temp
                return
            current = current.next
            temp = temp.next


