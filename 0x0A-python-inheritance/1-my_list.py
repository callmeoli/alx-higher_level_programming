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
        return self.sort()
