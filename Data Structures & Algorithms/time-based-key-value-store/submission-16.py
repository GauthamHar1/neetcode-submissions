from collections import defaultdict
class TimeMap:
    # ok so we want to be able to store k,v pairs but also have a time stamp associated 
    # with each value, what we could do is have a hashmap of hashmaps where the first hm
    # is key to hm and the second hm takes in timestamps and returns values

    # what if we store it in a list and then basically make each index a timestamp
    # 
    def __init__(self):
        self.kv_store = defaultdict(dict)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.kv_store[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key in self.kv_store:
            # so now we have a list of all timestamps and their values
            # we are given a timestamp input and we need to find the index
            # that is 
            hm = self.kv_store[key]
            lst = list(hm.keys())
            # we want to return "" if there are no keys in the hm that
            # are less than timestamp
             # we need to find the largest index with a value s.t. the index
            # is less than timestamp
            answer = -1
            print(hm,lst)
            l,r = 0,len(lst)-1
            while l<=r:
                mid = l+((r-l)//2)
                if lst[mid]<=timestamp:
                    answer = lst[mid]
                    l = mid+1
                else:
                    r = mid-1
            if answer!=-1:
                return hm[answer]
            else:
                return ""
    
        else:
            return ""
