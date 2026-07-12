class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def get_count(word:str) -> dict:
            count = {}
            for c in word:
                count[c] = count.get(c,0) + 1
            return count
        
        if get_count(s) == get_count(t):
            return True 
        return False