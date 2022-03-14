class Node:
  def __init__(self, key, value, next=None):
    self.key = key
    self.value = value
    self.next = None

class Hashtable:
  def __init__(self, size= 1024):
    self.size = size
    self.bucket = size *[None]
        # Initializer
      
  def add(self, key, value):
    hash_index = self.hash(key)
# comput the index of the key using the hash table
    if self.bucket[hash_index] is None:
# if bucket at index is empty, create a new node and add it there
      self.bucket[hash_index] = Node(key, value)
# otherwise a collusion happened; therefore we have to iterate to the end of the list and add a new node there.
    else:
      node = self.bucket[hash_index]
      if node.key == key:
        return
      else:
        while node.next:
          node =node.next
          if node.key == key:
            return
        node.next = Node(key, value)

  def get(self, key):
# retreive a data value stored under a certain key
# compute index for the provide key using the hash function.
    hash_index = self.hash(key)
# return None if not found
    if self.bucket[hash_index] is None:
      return None
    else:
# go to the bucket for that index
      node = self.bucket[hash_index] 
      if node.key == key:
# return value of the found node
        return node.value
      else:
        while node.next:
# iterate the nodes in that linked list until the key is found, or the end of the list is reached
          node = node.next
          if node.key == key:
            return node.value
        return None  

  def contains(self, key):
      # accept the key
    hash_index = self.hash(key)
    if self.bucket[hash_index] is None:
      return False
    else:
      node = self.bucket[hash_index]
      if node.key == key:
        return True
      else:
        while node.next:
          node = node.next
          if node.key == key:
            return True
          return False
        # contains
        # Arguments: key
        # Returns: Boolean, indicating if the key exists in the table already.

  def hash(self, key):
    return sum([ord(char) for char in key]) * 599 % self.size

  def keys():
    for collection in self.bucket:
      return print(collection)
