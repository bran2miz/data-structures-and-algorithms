from stacks_and_queue.stack_queue_brackets import validate_brackets
import pytest

def test_validate_parathesis():
    actual = True
    expected = validate_brackets('()')
    assert actual == expected

def test_validate_curly_brackets():
    actual = True
    expected = validate_brackets('{}')
    assert actual == expected

def test_validate_brackets():
    actual = True
    expected = validate_brackets('[]')
    assert actual == expected

def test_validate_multiple_brackets():
    actual = True
    expected = validate_brackets('(){}[[]]')
    assert actual == expected

def test_validate_code_fellows_brackets():
    actual = True
    expected = validate_brackets('{}{Code}[Fellows](())')
    assert actual == expected

def test_validate_false_brackets():
    actual = True
    expected = validate_brackets('[({}]')
    assert actual != expected

def test_validate_false_brackets_two():
    actual = True
    expected = validate_brackets('(](')
    assert actual != expected

def test_validate_false_brackets_three():
    actual = True
    expected = validate_brackets('{(})')
    assert actual != expected

def test_validate_is_empty():
    actual = True
    expected = validate_brackets('')
    assert actual == expected
