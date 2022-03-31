# Graphs

The code challenge assigned today gave us the opportunity to create our own graph and methods to add vertices, edges, and more.

## Challenge

In today's code challenge we had to implement our own Graph. The graph should be represented as an adjacency list.

## Approach & Efficiency

This code challenge was challenging, as we had to formulate code without any sort of pseudo code. I first took the approach of creating the add_node method. I then created the size method (seemingly easy as we were assigned to find the total number of nodes in the graph). Creating the methods were difficult.

The Big(O):
    time: O(1)
    space: O(n) because the amount of conversions grows depending on the amount of keys.

## API

We had to create the methods:

- an add_node method
Arguments: value
Returns: The added node
Add a node to the graph

- add edge method
Arguments: 2 nodes to be connected by the edge, weight (optional)
Returns: nothing
Adds a new edge between two nodes in the graph
If specified, assign a weight to the edge
Both nodes should already be in the Graph

- get_node method
Arguments: none
Returns all of the nodes in the graph as a collection (set, list, or similar)

get_neighbor method
Arguments: node
Returns a collection of edges connected to the given node
Include the weight of the connection in the returned collection

- size method
Arguments: none
Returns the total number of nodes in the graph

## Credit and Collaborators

Eddie Ponce

Alex Payne

Roger Huba

[Source](https://python-course.eu/applications-python/graphs-python.php)

[Source](https://www.educative.io/edpresso/how-to-implement-a-graph-in-python)
