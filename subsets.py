class Solution:
    def __init__(self):
        self.distinct = []
        
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if(nums is None or len(nums) == 0):
            return self.distinct
        collectList = []
        self.backtrack(nums, 0, collectList )
        return self.distinct 
    
    def backtrack(self, nums, index, collectList):
        #base
        if(index > len(nums) ):
            return
        
        #logic
        self.distinct.append(collectList[::])
        for i in range(index, len(nums)):
            collectList.append(nums[i])
            self.backtrack(nums, i+1, collectList)
            collectList.pop()