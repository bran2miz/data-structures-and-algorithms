# Stacks and Queues
    With the reading and the lecture from Monday, we were taught stack and queues. The idea of implementation (adding and removing items) might be the same, but the actual methodology is quite different.

    ex. Stack   4(pop function will remove top item)
                3
                2
                1(First in Last Out add item= push)
    ex. Queue
    4 -> 3 -> 2 -> 1 (First in First Out)

## Challenge

The challenge was to create several different stack and queue functions that:

-Added item/s to the Stack or Queue

-Removed item/s from the Stack or Queue

-Peek the Stack(top) or the Queue(front)

-Raised Exception within the Peek or Remove function in case the Stack or Queue were Empty

- Create a function that that checks to see if the Stack or Queue was empty (True or False)

## Approach & Efficiency

The approach I first took was to look at the pseudo code that was provided in the class repo.

I then created separate files for the Node, Queue, and Stack classes.

Doing some refracturing from the psuedo code, I was able to create a solid base code to run some tests with.

Tests were made to compare whether the actual value was returning the expected value

Big O:
time: O(1)
space: change based on the function ie push (O(n))

## API

### Stack

**Push** - Node or items placed into a stack are pushed.

**Pop**- function where Node or items removed from a stack.

**isEmpty**- function that returns True if empty stack; False if not empty.

**Peek**- function to view the top Node's value.exception is raised in case there is an empty queue.

### Queue

**Enqueue**- Node or items added into queue

**Dequeue**- Node or items removed from the queue.

**Peek**- view first Node of the queue. An exception is raised in the beginning in case of an empty queue.

**isEmpty**- returns true when queue is empty; false if not empty.

Collaborators:

Alex Payne
Eddie Ponce
Connor Boyce
Kassie Bradshaw
Roger Huba
