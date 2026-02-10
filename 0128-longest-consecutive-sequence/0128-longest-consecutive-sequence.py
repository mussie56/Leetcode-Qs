class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = 0
        num_set = set(nums)
        for num  in num_set:
            if num-1 not in num_set:
                current = num
                streak = 1
                while current+1 in num_set:
                    streak+=1
                    current+=1
                count = max(count,streak)

        return count