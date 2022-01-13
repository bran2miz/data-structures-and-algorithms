from stacks_and_queue.node import Node

class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        self.top = Node(value)
        return self.top
        # // INPUT <-- value to add, wrapped in Node internally
        # //OUTPUT <-- none
        # node = new Node(value)
        # node.next <-- Top
        # top <-- Node

    def pop(self):
            #         // INPUT <-- No input
    # // OUTPUT <-- value of top Node in stack
    # // EXCEPTION if stack is empty

    #    Node temp <-- top
    #    top <-- top.next
    #    temp.next <-- null
    #    return temp.value
        try:
            temp = self.top
            self.top = None
            return temp.value
        except:
            if self.top == None:
                return Exception




    def peek(self):
    #         ALGORITHM peek()
    # // INPUT <-- none
    # // OUTPUT <-- value of top Node in stack
    # // EXCEPTION if stack is empty
    #    return top.value
        if self.top == None:
            raise Exception
        return self.top.value

    def isEmpty(self):
        #         ALGORITHM isEmpty()
    # // INPUT <-- none
    # // OUTPUT <-- boolean

    # return top = NULL
        return self.top is None


