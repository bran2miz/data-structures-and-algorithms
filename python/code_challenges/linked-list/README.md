# Singly Linked List

In class we learned about the idea of linked lists and classes. We also learned about the idea that all of the nodes do not have any other information except for their own value and the value of the next node.

## Challenge

This challenge includes linked lists that is comprised of classes. These lists will allow the user to implement addition nodes with values to the list search. If the value is part of the list search, it will append all of the values of all the nodes.

## Approach & Efficiency

Big O
time: 0(n)
space: log(n)

## API

The insert() function creates new nodes. If a node exists as a value within the linked list, it will "insert" the created node, but will set that node as the new head and push the existing ones behind.

The includes() function will navigate through the linked lists for nodes with the same values. If the linked list value and the current value match it will be set to True; otherwise the value will return false.

The to_string function will begin at the head of the linked list and look through all the nodes. The function will then take the current value of that node. By implementing a f string, it will push the matching values into the curly brackets {}.

## Collaborators

Michael Greene
Alex Payne
Eddi Ponce
Connor Bryce

Sources:
[Source](https://www.w3schools.com/python/ref_string_format.asp)
