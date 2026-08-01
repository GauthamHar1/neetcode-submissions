class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # we can do a modified binary search here
        # so we can start at the very middle of the middle
        # of the array so we can have a top down ptr and 
        # a left right ptr

        u,l = 0,0
        d,r = len(matrix)-1,len(matrix[0])-1
        print(d,r)

        while u<=d:
            mid = u+((d-u)//2)
            if target >= matrix[mid][l] and target<=matrix[mid][r]:
                while l<=r:
                    mid1 = l+((r-l)//2)
                    if matrix[mid][mid1] == target:
                        return True
                    elif matrix[mid][mid1] < target:
                        l = mid1+1
                    else:
                        r = mid1-1
                return False
            elif target > matrix[mid][r]:
                u = mid+1
            else:
                d = mid-1
        return False
            

        