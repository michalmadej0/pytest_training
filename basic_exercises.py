from code_to_test import add_numbers, add_number2, multi_number, is_adult
def test_add_numbers():
    a = 4
    b = 7
    exepected = 11
    assert add_numbers(a, b) == exepected

def test_add_numbers_negative_value():
    a = -5
    b = -100
    expected = -105
    assert add_numbers(a, b) == expected

def test_add_number_sam():
    a = 0
    b = 0
    expected = 0
    assert add_numbers(a, b) == expected
def test_add_number2():
    a = 10
    b = 10
    expected = 1
    assert add_number2(a,b) == expected

def test_multi_number():
    a = -2
    b = 2
    expected = -4
    assert multi_number(a, b) == expected
def test_is_adult():
    age = 18
    assert is_adult(age)
    assert is_adult(55)
    assert is_adult(135)
def test_is_not_adult():
    age = 15
    expected = False
    assert is_adult(age) == expected
    assert is_adult(0) == expected
    assert is_adult(-10) == expected
    assert is_adult(17) == expected

