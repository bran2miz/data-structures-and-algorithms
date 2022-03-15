# Hashtables
Today we learned about hashtables.

```python
Key = "Cat"
Value = "Josie"

67 + 97 + 116 = 280

280 * 599 = 69648

69648 % 1024 = 16

Key gets placed in index of 16. 
```

## Challenge

New Implementation

Implement a Hashtable Class with the following methods:

set
Arguments: key, value
Returns: nothing
This method should hash the key, and set the key and value pair in the table, handling collisions as needed.
Should a given key already exist, replace its value from the value argument given to this method.

get
Arguments: key
Returns: Value associated with that key in the table

contains
Arguments: key
Returns: Boolean, indicating if the key exists in the table already.

keys
Returns: Collection of keys

hash
Arguments: key
Returns: Index in the collection for that key


## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
This assignment was pretty difficult as we were not given much starter code. I first looked online for some examples of how to incorporate linked list into my approach. Once I was able to get a better grasp on hashtables, it became easier to manage code. The Big O approach is O(1) time complexity and O(n) space complexity.


## API

Add()
When adding a new key/value pair to a hashtable:

send the key to the GetHash method.
Once you determine the index of where it should be placed, go to that index
Check if something exists at that index already, if it doesn’t, add it with the key/value pair.
If something does exist, add the new key/value pair to the data structure within that bucket.
Find()
The Find takes in a key, gets the Hash, and goes to the index location specified. Once at the index location is found in the array, it is then the responsibility of the algorithm the iterate through the bucket and see if the key exists and return the value.

Contains()
The Contains method will accept a key, and return a bool on if that key exists inside the hashtable. The best way to do this is to have the contains call the GetHash and check the hashtable if the key exists in the table given the index returned.

GetHash()
The GetHash will accept a key as a string, conduct the hash, and then return the index of the array where the key/value should be placed.


## Credits and Collaborators

Alex Payne

Michael Greene

Eddie Ponce

Connor Boyce

[Source](https://www.youtube.com/watch?v=zHi5v78W1f0)

