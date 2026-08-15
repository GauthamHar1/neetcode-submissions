from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left,best = 0,0
        counts = defaultdict(int)
        # for each window, we can check which letter there is the most of,
        # then for the remaining letters, we can just count how many there are
        # and check that its less than k

        for right in range(len(s)):
            counts[s[right]]+=1
            max_pair = ("",0)
            total = 0
            for key,val in counts.items():
               
                if val>=max_pair[1]:
                    max_pair = (key,val)
                total+=val
            # print("max pair and total", max_pair,total)
            # if the num of elements other than the main one is greater than k,
            # then the window is invalid
            while total-max_pair[1]>k:
                counts[s[left]]-=1
                # if the leftmost element is the max, we have to recompute the max
                max_pair = ("", 0)
                for key,val in counts.items():
                    if val>=max_pair[1]:
                        max_pair = (key,val)
                
                total-=1
                left+=1
            best = max(right-left+1,best)
            
        return best
            # now we have the key with the max valu


