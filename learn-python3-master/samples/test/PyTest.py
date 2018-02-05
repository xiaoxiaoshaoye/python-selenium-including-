#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import  pytest


def reverse(string):
                  return  string[::-1]
def test_reverse():
                 string = "good"
                 assert reverse(string) == "doog"
                 string2 = "erha"
                 assert  reverse(string2) == "erha"
def f():
    return 3

def test_function():
    assert f() == 4

def test_zero_division():
        with pytest.raises(ValueError):
            1 / 3
def test_recursion_depth():
    with pytest.raises(RuntimeError) as excinfo:
         def f():
             f()
if __name__ == '__main__':
    pytest.main("PyTest.py")
