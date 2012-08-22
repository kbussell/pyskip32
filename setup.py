#!/usr/bin/env python

from distutils.core import setup, Extension

module1 = Extension('skip32', sources = ['skip32.c'])

setup (name = 'skip32',
        version = '1.0',
        description = 'implementation of skip32 based on http://search.cpan.org/~esh/Crypt-Skip32-0.08/lib/Crypt/Skip32.pm',
        ext_modules = [module1],
        author = 'Keith Bussell')
