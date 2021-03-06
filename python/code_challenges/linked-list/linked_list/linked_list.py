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

    def __str__(self):
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

    def append(self, new_value):
        if self.head is None: #If linked-list is empty make this the head
            self.head = Node(new_value)
        else:
            current = self.head
            while(current.next):
                current = current.next
            current.next = Node(new_value)

    def insert_before(self, target, new_value):
        if self.head and self.head.value == target:
            new_node = Node(new_value, self.head)
            self.head = new_node
        elif self.head:
            current = self.head
            previous = Node(None, current)
            while(current and current.value != target):
                current = current.next
                previous = previous.next
            if current and current.value == target:
                new_node = Node(new_value, current)
                previous.next = new_node
            else: #if this else block is reached we did not find target
                raise Exception('Target not found in LinkedList')

    def insert_after(self, target, new_value):
        if self.head:
            current = self.head
            next_node = current.next
            while(current and current.next and current.value != target):
                current = current.next
                next_node = next_node.next
            if current and current.value == target:
                new_node = Node(new_value, next_node)
                current.next = new_node
            else:
                raise Exception('Target value not found in LinkedList')

    def kth_from_end(self, k):
        if k < 0:
            return IndexError
        else:
            current = self.head
            values = []
            while current:
                values.append(current.value)
                current = current.next
            if k > len(values):
                return None
            else: return values[-k-1]

    def linked_list_zip(list_1, list_2):
        if list_1.head == None and list_2.head == None:
            return None
        elif list_1.head is None:
            return list_2
        elif list_2.head is None:
            return list_1
        new_linked_list = LinkedList()
        linked_list_1 = list_1.head
        linked_list_2 = list_2.head
        while linked_list_1 or linked_list_2:
            if linked_list_1:
                new_linked_list.append(linked_list_1.value)
                linked_list_1 = linked_list_1.next
            if linked_list_2:
                new_linked_list.append(linked_list_2.value)
                linked_list_2 = linked_list_2.next

        return new_linked_list
