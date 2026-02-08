class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
       dup=list(set(nums))
       if(len(nums)==len(dup)):
        return False
       else:
        return True