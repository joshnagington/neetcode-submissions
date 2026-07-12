class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        keys = {}
        for word in strs:
            # Convert the sorted list of characters into a tuple so it can be a dictionary key
            key = tuple(sorted(word))
            keys.setdefault(key, [])
            keys[key].append(word)
            
        # Return all the grouped lists
        return list(keys.values())
