import pytest
import pangram

pangrams = [
"aaaabcdefgh{ijk}lmnop`qrstuvwxyz!FDA$43918 4321~[]",
"abcdefghijkl{mnopqr`}stuvWXyZ",
"abcdefghijklmnopqrstuvWXyZ"
]
non_pangrams = [
"aaabcdef}g{hijklmnop`qrstuvwxy",
"abcdeda}{ghi11321,.d`   ;13`~fa836;{lxy",
"abcd",
''
]

def test_pangram_a():
    for p in pangrams:
        assert pangram.check_if_pangram_a(p)
    for p in non_pangrams:
        assert ~pangram.check_if_pangram_a(p)

def test_pangram_b():
    for p in pangrams:
        assert pangram.check_if_pangram_b(p)
    for p in non_pangrams:
        assert ~pangram.check_if_pangram_b(p)

def test_pangram_c():
    for p in pangrams:
        assert pangram.check_if_pangram_c(p)
    for p in non_pangrams:
        assert ~pangram.check_if_pangram_c(p)

