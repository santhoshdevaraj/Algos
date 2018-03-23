# Write a function that takes a string as input and returns the string reversed.

# Example:
# Given s = "hello", return "olleh".

class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)

        i, j = 0, len(s) - 1

        while i <= j:
        	s[i], s[j] = s[j], s[i]
        	i += 1
        	j -= 1

        return ''.join(s)

print Solution().reverseString('abc')
