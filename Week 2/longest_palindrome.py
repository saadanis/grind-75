from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:

        longest_overall = 0
        additional_one = 0

        for count in Counter(s).values():
            if count%2 == 0:
                longest_overall += count
            else:
                if count > 1:
                    longest_overall += count - 1
                additional_one = 1
        
        return longest_overall + additional_one