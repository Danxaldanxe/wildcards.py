#!/usr/bin/env python
from unittest import main, TestCase
from assert_is import not_, ok_
from wildcards import fnmatch, filter

class Test(TestCase):
    def test_filter(self):
        files=["file1.py","file2.py","file2.pyc",".gitignore"]
        patterns=["*.py","*.pyc"]
        filtered=filter(files,patterns)
        for f in filtered:
            ok_(fnmatch(f,patterns))
        pattern=patterns[0]
        filtered=filter(files,pattern)
        for f in filtered:
            ok_(fnmatch(f,pattern))

if __name__ == "__main__": # pragma: no cover
    main()