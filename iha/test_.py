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