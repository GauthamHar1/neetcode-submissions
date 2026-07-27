class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            l = len(s)
            result+=str(l)
            result+="|"
            result+=s
            
        return result

        
        # incorporate the length of each word,
        # but how to differentiat 
    def decode(self, s: str) -> List[str]:
        result = []
        i=0
        print(s)
        while i<len(s):
            # we need to set the cur_len to the number 
            # before the "|"
            # k should get to the index of "|"
            k = 0
            while s[i+k]!="|":
                k+=1
            cur_len = int(s[i:i+k])
            print(cur_len)
            if cur_len == 0:
                result.append("")
            else:
                cur_word = s[i+k+1:i+cur_len+k+1]
                print(cur_word)
                result.append(cur_word)
            i += cur_len+k+1
        return result
