# Given a string S, we can transform every letter individually to be lowercase or uppercase 
# to create another string.  Return a list of all possible strings we could create.

# Examples:
# Input: S = "a1b2"
# Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

# Input: S = "3z4"
# Output: ["3z4", "3Z4"]

# Input: S = "12345"
# Output: ["12345"]
# Note:

# S will be a string with length at most 12.
# S will consist only of letters or digits.

import string

class Solution(object):
    def letterCasePermutation(self, s):
        """
        :type S: str
        :rtype: List[str]
        """
        if not s:
        	return [s]

        if s[0] in string.ascii_lowercase or s[0] in string.ascii_uppercase:
        	return [s[0].upper() + i for i in self.letterCasePermutation(s[1:])] + [s[0].lower() + i for i in self.letterCasePermutation(s[1:])]
        else:
        	return [s[0] + i for i in self.letterCasePermutation(s[1:])]

print Solution().letterCasePermutation("C")
