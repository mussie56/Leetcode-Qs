class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mapp = Counter(nums)

        ans = [key for key,val in mapp.items() if val > len(nums)//2]

        return ans[0] 