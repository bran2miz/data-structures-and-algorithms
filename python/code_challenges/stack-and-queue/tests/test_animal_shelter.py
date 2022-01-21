from  stacks_and_queue.animal_shelter import AnimalShelter

def test_animal_shelter():
    animal_shelter = AnimalShelter()
    assert animal_shelter

def test_animal_shelter_enqueue_cat():
    animal_shelter = AnimalShelter()
    animal_shelter.enqueue('cat')
    actual = animal_shelter.in_stack.peek()
    expected = 'cat'
    assert actual == expected

def test_animal_shelter_enqueue_dog():
    animal_shelter = AnimalShelter()
    animal_shelter.enqueue('dog')
    actual = animal_shelter.in_stack.peek()
    expected = 'dog'
    assert actual == expected

def test_animal_shelter_enqueue_multiple():
    animal_shelter = AnimalShelter()
    animal_shelter.enqueue('dog')
    animal_shelter.enqueue('cat')
    actual = animal_shelter.in_stack.peek()
    expected = 'dog'
    assert actual == expected

def test_animal_shelter_enqueue_return_none():
    animal_shelter = AnimalShelter()
    animal_shelter.enqueue('dog')
    actual = animal_shelter.in_stack.peek()
    expected = 'cat'
    assert actual != expected

def test_animal_shelter_dequeue():
    animal_shelter = AnimalShelter()
    animal_shelter.enqueue('dog')
    animal_shelter.enqueue('cat')
    animal_shelter.enqueue('cat')
    actual = animal_shelter.dequeue('cat')
    expected = 'cat'
    assert actual == expected
