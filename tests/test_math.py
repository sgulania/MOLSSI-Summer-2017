"""
Testing for the math.py module
"""

import MOLSSI_SUMMER_2017 as ms
import pytest

def test_add():
    assert ms.math.add(5,2) == 7
    assert ms.math.add(2,5) == 7

def test_sub():
    assert ms.math.sub(5,2) == 3
    assert ms.math.sub(2,5) == -3

def test_mult():
    assert ms.math.mult(5,2) == 10
    assert ms.math.mult(2,5) == 10

def test_div():
    assert ms.math.div(4,2) == 2
    assert ms.math.div(6,2) == 3
