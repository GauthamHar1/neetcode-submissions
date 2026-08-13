from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left,best = 0,0
        counts = defaultdict(int)

        for right in range(len(s)):
            counts[s[right]]+=1
            # while window is invalid we increment left
            while left<right and counts[s[right]]>1:
                counts[s[left]]-=1
                left+=1
            best = max(right-left+1,best)
                
        
        return best
            
            
