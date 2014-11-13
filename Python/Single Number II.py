import os, sys

"""
https://oj.leetcode.com/problems/single-number-ii/

Given an array of integers, every element appears three times except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

"""


class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        numhash={}
        for i in A:
            if not numhash.has_key(i):
                numhash[i] = 1
            elif numhash[i] == 2:
                numhash.pop(i)
            else:
                numhash[i] += 1
        return numhash.keys()[0]
