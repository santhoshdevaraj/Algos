# Write a function to generate the generalized abbreviations of a word.

# Example:
# Given word = "word", return the following list (order does not matter):
# ["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]

import re

class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        if not word: return [word]

        output = []

        abbrs = self.generateAbbreviations(word[1:])
        
        for abbr in abbrs:
            output.append(word[0]+abbr)
            if abbr and abbr[0].isdigit():
                leading_int = re.search(r'\d+', abbr).group()
                output.append(str(1 + int(leading_int)) + abbr[len(leading_int):])
            else:
                output.append('1' + abbr)

        return output
