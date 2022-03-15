class Hashtable:
  def __init__(self, size=1024):
    self.size= size
    self.bucket = size * [None]
  
  def set(self, key, value):
    hash_index = self.hash(key)

    if self.bucket[hash_index] == None:
      self.bucket[hash_index] = {}
    
    self.bucket[hash_index][key] = value
  
  def get(self, key):
    hash_index = self.hash(key)

    if self.bucket[hash_index] == None:
      return None
    
    for idx in self.bucket[hash_index]:
      if idx == key:
        return self.bucket[hash_index][key]
    
    return None
  
  def contains(self,key):
    hash_index = self.hash(key)

    if self.bucket[hash_index] == None:
      return False
    
    for idx in self.bucket[hash_index]:
      if idx == key:
         return True
    
    return False
  
  def hash(self, key):

    sum = 0

    if isinstance(key, int):
      raise Exception('Cannot compute numbers')
    
    for ch in key:
      if isinstance(ch, int):
        sum += ch
      else:
        sum += ord(ch)
  
    primed = sum * 97
    index = primed % self.size

    return index

  def keys(self):
    key_list = []

    for idx in self.bucket:
      if idx != None:
        temp = [*idx]
        key_list += temp
    
    return key_list

    
