import pytest
import roman_numeral

test_roman=[
    ('IX',9),
    ('MXIII',1013),
    ('MXLIII',1043),
    ('CMIII',903),
    ('V',5),
    ('MMMCCLXXI',3271),
    ('I',1),
    ('IV',4),
]

def test_roman_numeral():
    assert roman_numeral.convert_roman_numeral('MXIIII') == 1014
    assert roman_numeral.convert_roman_numeral('MXIIII') == 1014

def test_roman_numeral_2():
    for n in test_roman:
        rom, val = n
        assert roman_numeral.convert_roman_numeral_2(rom) == val

def test_roman_numeral_3():
    for n in test_roman:
        rom, val = n
        assert roman_numeral.convert_roman_numeral_3(rom) == val

"""
def test_shorten_roman_numeral():
    test_short=[
        #('IIIII','V'),
        #('IIIIIIII','VIII'),
        ('XVVIIIII','XXV')
    ]
    for n in test_short:
        long, short = n
        assert roman_numeral.short_roman_numeral(long) == short
"""