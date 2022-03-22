from hash_left_join import hashmap_left_join

def test_import():
    assert hashmap_left_join

def test_left_join():
    synonyms = {'happy': 'joyful'}
    antonyms = {'happy': 'sad'}
    assert hashmap_left_join(synonyms, antonyms) == ['happy', 'joyful', 'sad']

def test_left_join_more():
    synonyms = {'happy': 'joyful','scared':'afraid'}
    antonyms = {'happy': 'sad','scared':'brave'}

    assert hashmap_left_join(synonyms, antonyms) == ['happy', 'joyful', 'sad',
                                             'scared', 'afraid', 'brave']

def test_left_join_with_none():
    synonyms = {'happy': 'joyful','scared':'afraid','mad':'angry'}
    antonyms = {'happy': 'sad','scared':'brave'}

    assert hashmap_left_join(synonyms, antonyms) == ['happy', 'joyful', 'sad',
                                             'scared', 'afraid', 'brave',
                                             'mad', 'angry', None]
