# Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.


# American keyboard


# Example 1:
# Input: ["Hello", "Alaska", "Dad", "Peace"]
# Output: ["Alaska", "Dad"]
# Note:
# You may use one character in the keyboard more than once.
# You may assume the input string will only contain letters of alphabet.


class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        
        return filter(lambda x: all(c in 'qwertyiuop' for c in x.lower()) or all(c in 'asdfghjkl' for c in x.lower()) or all(c in 'zxcvbnm' for c in x.lower()), words)

print Solution().findWords(["Hello", "Alaska", "Dad", "Peace"])