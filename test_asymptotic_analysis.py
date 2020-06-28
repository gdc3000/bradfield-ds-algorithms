import pytest
import asymptotic_analysis as aa


def test_factorial():
    assert aa.factorial_1(5) == 5*4*3*2
    assert aa.factorial_2(5) == 5*4*3*2