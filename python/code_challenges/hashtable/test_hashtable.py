from hashtable import Hashtable
import random

def test_hashtable_add_function():
    hashtable = Hashtable()
    hashtable.add('key', 'value')
    assert hashtable.contains('key') == True

def test_hashtable_get_function():
    hashtable = Hashtable()
    hashtable.add('key', 'value')
    assert hashtable.get('key') == 'value'

def test_hashtable_get_none():
    hashtable = Hashtable()
    assert hashtable.get('key') is None

def test_hashtable_contains_none():
    hashtable = Hashtable()
    assert hashtable.contains('key') == False

def test_hashtable_add_contains_value_collision():
    hashtable = Hashtable()
    hashtable.add('key', 'value')
    hashtable.add('yke', 'yek value')
    assert hashtable.contains('yke') is True
    assert hashtable.contains('yke') is True
    assert hashtable.hash('key') == hashtable.hash('yke')


# Successfully retrieve a value from a bucket within the hashtable that has a collision
def test_hashtable_add_get_value_collision():
    hashtable = Hashtable()
    hashtable.add('key', 'value')
    hashtable.add('yek', 'yek value')
    assert hashtable.get('key') == 'value'
    assert hashtable.get('yek') == 'yek value'
    assert hashtable.hash('key') == hashtable.hash('yek')

# Successfully hash a key to an in-range value
def test_hashtable_hash_in_range():
    hashtable_size=1024
    hashtable = Hashtable(hashtable_size)
    random_keys = [''.join([chr(random.randint(32, 127)) for char in range(random.randint(0,30))]) for _ in range(1000)]
    for key in random_keys:
        assert hashtable.hash(key) in range(hashtable_size)