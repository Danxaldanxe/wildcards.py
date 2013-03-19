#!/usr/bin/env python
from unittest import main, TestCase
from assert_is import not_, ok_
from wildcards import fnmatch

class Test(TestCase):
    def test_fnmatch(self):
        patterns=["*.py","*.pyc"]
        ok_(fnmatch("file.py",patterns))
        not_(fnmatch(".gitignore",patterns))
        pattern=patterns[0]
        ok_(fnmatch("file.py",pattern))
        not_(fnmatch(".gitignore",pattern))

if __name__ == "__main__": # pragma: no cover
    main()