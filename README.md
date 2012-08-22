pyskip32
========

Wraps the original c implementation of skip32 by Greg Rose, QUALCOMM Australia with a thin layer of python.

Example Usage
=============

```python
>>> import random
>>> import skip32
>>> key = ''.join(chr(random.randint(0, 255)) for _ in xrange(10))
>>> encrypted = skip32.encrypt(key, 12345)
>>> encrypted
3798503945L
>>> skip32.decrypt(key, encoded)
12345L
```
