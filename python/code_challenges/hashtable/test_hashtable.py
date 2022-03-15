from hashtable import Hashtable

import pytest

def test_hashtable():
    hashtable = Hashtable()
    hashtable.set('key', 24)
    expected = True 
    actual = hashtable.contains('key') == True
    assert actual == expected

def test_get_key():
    hashtable = Hashtable()
    hashtable.set('key', 24)
    expected = 24
    actual = hashtable.get('key')
    assert actual == expected

def test_no_hash_in_table():
    hashtable = Hashtable()
    hashtable.set('key', 8)
    expected = None
    actual = hashtable.get('value')
    assert actual == expected

def test_key_list():
    hashtable = Hashtable()
    hashtable.set('k', 8)
    hashtable.set('e', 7)
    hashtable.set('y', 6)
    hashtable.set('a', 9)
    hashtable.set('b', 2)
    actual = hashtable.keys()
    expected = ['k', 'a', 'b', 
    'y', 'e']
    assert actual == expected

def test_collision():
    hashtable = Hashtable()
    hashtable.set('key', 10)
    hashtable.set('kye', 11)

    actual = hashtable.contains('key')
    expected = True
    assert actual == expected

    actual = hashtable.contains('kye')
    expected = True
    assert actual == expected

def test_collision_two():
    hashtable = Hashtable()
    hashtable.set('value', 20)
    hashtable.set('vuela', 21)
    hashtable.set('eluav', 22)

    actual = hashtable.get('value')
    expected = 20
    assert actual == expected

    actual = hashtable.get('vuela')
    expected = 21
    assert actual == expected

    actual = hashtable.get('eluav')
    expected = 22
    assert actual == expected

def test_hashtable_two():
    hashtable = Hashtable()
    hashtable.set('value', 22)
    expected = True
    actual = hashtable.contains('value') == True
    assert actual == expected
