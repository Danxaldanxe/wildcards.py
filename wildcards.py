#!/usr/bin/env python
from fnmatch import fnmatch as _fnmatch
from fnmatch import filter as _filter

def fnmatch(filename, pattern):
    """fnmatch replacement for accept pattern list"""
    if isinstance(pattern,list):
        for p in pattern:
            if _fnmatch(filename,p):
                return True
        return False
    else:
        return _fnmatch(filename, pattern)

def filter(names, pattern="*"):
    """fnmatch.filter replacement for accept pattern list"""
    if isinstance(pattern,list):
        result=[]
        for p in pattern:
            result+=_filter(names, p)
        return result
    else:
        return _filter(names, pattern)

def ignore(names, pattern=None):
    if pattern:
        if isinstance(pattern,list):
            ignored=[]
            for p in pattern:
                ignored+=_filter(names, p)
        else:
            ignored=_filter(names, pattern)
        for i in ignored:
            try:
                names.remove(i)
            except:
                pass
    return names
