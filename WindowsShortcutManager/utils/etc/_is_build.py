import sys

def is_bundled():
    return hasattr(sys, 'frozen')