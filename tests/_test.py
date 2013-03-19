#!/usr/bin/env python
from wildcards import fnmatch, filter,ignore


from dir import files
list=files(
    "~/git/python/vlc.py",
    tree=True,
    ignore="*test*"
)
print list
#print ignore(list,"*test*")