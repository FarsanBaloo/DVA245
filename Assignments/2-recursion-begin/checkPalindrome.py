# -*- coding: utf-8 -*-
"""
TODO: implement recursiveCheckPalindrome

"""


def recursiveCheckPalindrome(word: str):

    if len(word) <= 3 and word[0].lower() == word[-1].lower():
        return True
    elif word[0].lower() == word[-1].lower():
       return recursiveCheckPalindrome(word[1:-1])
    else:
        return False

    # TODO implement
    # What is the base case?
    # How can we solve a small part of the problem
    # and call recursiveCheckPalindrome with a subset of the
    # initial problem?
    # Use lower() to make the method case insensitive
    # return True if word is a palindrome, False otherwise
    # return


