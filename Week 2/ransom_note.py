from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r = Counter(ransomNote)
        m = Counter(magazine)

        for l in r:
            if m[l] - r[l] < 0:
                return False
        
        return True