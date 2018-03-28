# Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

# For example,
# Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

# Given word1 = “coding”, word2 = “practice”, return 3.
# Given word1 = "makes", word2 = "coding", return 1.

# Note:
# You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.


class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        word1_idx = word2_idx = None

        distance = len(words)

        for idx, word in enumerate(words):
            if word == word1:
                word1_idx = idx
            if word == word2:
                word2_idx = idx
            if word1_idx is not None and word2_idx is not None:
                distance = min(distance, abs(word2_idx - word1_idx))
        
        return distance


print Solution().shortestDistance(["practice", "makes", "perfect", "coding", "makes"], 'makes', 'practice')

