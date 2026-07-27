class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # ok so im immediately thinking how is this dif
        # from two sum, what does the fact that its sorted mean
        # since we must use O(1) additional space, a hashmap
        # wont work lets try 2 ptrs, both start at index 1 and 2
        # then if that is less than target then we keep p1 and incr
        # p2 and if its greater than target we incr p1 and keep p2 until
        # its less than or equal to target
        p1,p2=0,(len(numbers)-1)
        
        while p2>p1:
            cur_sum = numbers[p1]+numbers[p2]
            if cur_sum==target:
                return [p1+1,p2+1]
            elif cur_sum<target:
                p1+=1
            else:
                p2-=1
                
        
        return []
            
            
            

        
        
