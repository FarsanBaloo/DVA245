# -*- coding: utf-8 -*-
"""
TODO: implement recursiveCheckPalindrome

"""

def recursiveCheckPalindrome(word):

    if len(word) <= 1:
        return True

    if word[0].lower() == word[-1].lower():
       recursiveCheckPalindrome(word[1:-1])
    else:
        return False

    # TODO implement
    # What is the base case?
    # How can we solve a small part of the problem
    # and call recursiveCheckPalindrome with a subset of the
    # initial problem?
    # Use lower() to make the method case insensitive
    # return True if word is a palindrome, False otherwise
    return 


