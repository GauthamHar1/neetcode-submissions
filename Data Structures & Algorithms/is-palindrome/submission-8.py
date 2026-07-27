class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = "".join(c for c in s if c.isalnum()).lower()
        p1 = 0
        p2 = len(clean)-1
        while p2>=p1:
            if clean[p1]!=clean[p2]:
                print(clean[p1],clean[p2])
                return False
            p2-=1
            p1+=1
        return True