import pytest
from kata import Add

def test_empty_sting():
    assert Add("") == 0

def test_one_integer():
    assert Add("1") == 1
    assert Add("45") == 45
    assert Add("101") == 101

def test_two_integers():
    assert Add("1,2") == 3
    assert Add("10,5") == 15
    assert Add("99,9") == 108

def test_many_integers_with_comma():
    assert Add("1,2,3") == 6
    assert Add("5,10,100,23,7") == 145
    assert Add("7,5,49,5") == 66

def test_many_integers_with_newline():
    assert Add("1\n2,3") == 6
    assert Add("50,10\n3") == 63
    assert Add("8\n2\n22,3") == 35

def test_numbers_bigger_than_thousand():
    assert Add("1001,2") == 2
    assert Add("3\n3000") == 3
    assert Add("1000,500\n1042") == 1500