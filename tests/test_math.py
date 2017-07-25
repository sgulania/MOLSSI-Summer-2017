"""
Testing for the math.py module
"""

import MOLSSI_SUMMER_2017 as ms
import pytest

def test_add():
    assert ms.math.add(5,2) == 7
    assert ms.math.add(2,5) == 7



