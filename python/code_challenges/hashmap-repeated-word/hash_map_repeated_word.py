from code_challenges.hashtable.hashtable import Hashtable

def hashmap_repeated_word(text):
  words = ''
  hashmap = Hashtable()
  for word in text:
    lower_word = word.lower()
    if ord(lower_word) in range(ord('a'), ord('z') + 1):
      words += lower_word
    elif len(words):
      if hashmap.contains(words):
        return words
      else:
        hashmap.set(words, None)
        words= ''
  if len(words) and hashmap.contains(words):
    return words
  return None