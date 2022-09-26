#!/usr/bin/python3
"""
This module include that print list in sorted order
"""


class MyList(list):
    """
    This class contain print sorted list
    """
    def print_sorted(self):
        """
        print sorted list
        """
        l_sorted = self.copy()
        l_sorted.sort()
        print(l_sorted)
