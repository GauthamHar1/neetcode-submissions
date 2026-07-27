from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # new idea, make a hashmap, where
        # the key is a hashmap that keeps track
        # of frequency of each char, and the 
        # value is list of matching strs
        groups = defaultdict(list)
        for word in strs:
            groups["".join(sorted(word))].append(word)
        return list(groups.values())
        
        