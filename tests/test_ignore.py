#!/usr/bin/env python
from unittest import main, TestCase
from assert_is import not_, ok_
from wildcards import fnmatch, ignore

class Test(TestCase):
    def test_ignore(self):
        files=["file1.py","file2.py","file2.pyc",".gitignore"]
        patterns=["*.py","*.pyc"]
        filtered=ignore(files,patterns)
        for f in filtered:
            not_(fnmatch(f,patterns))
        pattern=patterns[0]
        filtered=ignore(files,pattern)
        for f in filtered:
            not_(fnmatch(f,pattern))

    def test(self):
        pass

if __name__ == "__main__": # pragma: no cover
    main()