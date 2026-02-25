class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s=set()

        #for i,num in enumerate(nums):
            
 
        for num in nums:
            if num in s:
                return True

            s.add(num)
        return False

