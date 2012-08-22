#!/usr/bin/env python

__test__ = {'tokenizer_tests': """
>>> import skip32
>>> skip32.encrypt('1234567890', 1)
116993676

>>> skip32.decrypt('1234567890', 116993676)
1
"""}

def _test():
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    _test()
