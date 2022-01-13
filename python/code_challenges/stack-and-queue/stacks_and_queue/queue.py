from stacks_and_queue.node import Node

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
     #         ALGORITHM enqueue(value)
    # // INPUT <-- value to add to queue (will be wrapped in Node internally)
    # // OUTPUT <-- none
    #    node = new Node(value)
    #    rear.next <-- node
    #    rear <-- node
        node = Node(value)

        if not self.rear:
            self.rear = node
            self.front = node

        self.rear.next = node


    def dequeue(self):
    #         ALGORITHM dequeue()
    # // INPUT <-- none
    # // OUTPUT <-- value of the removed Node
    # // EXCEPTION if queue is empty

    #    Node temp <-- front
    #    front <-- front.next
    #    temp.next <-- null

    #    return temp.value
        if not self.front:
            raise Exception

        temp = self.front
        self.front = self.front.next
        temp.next = None
        return temp.value


    def peek(self):
    #         ALGORITHM peek()
    # // INPUT <-- none
    # // OUTPUT <-- value of the front Node in Queue
    # // EXCEPTION if Queue is empty
    #    return front.value
        if not self.front:
            raise Exception

        return self.front.value


    def isEmpty(self):
        return self.front is None
    #     ALGORITHM isEmpty()
    # // INPUT <-- none
    # // OUTPUT <-- boolean

    # return front = NULL
