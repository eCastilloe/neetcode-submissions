class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numset = set(nums)
        l = len(nums)
        if len(numset) < l:
            return True
        return False
        
            
        