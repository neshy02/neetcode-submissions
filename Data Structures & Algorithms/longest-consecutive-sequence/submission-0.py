class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len = 0
        set_nums = set(nums)

        for num in set_nums:
            if (num - 1) not in set_nums:
                curr = num
                streak = 1

                while (curr + 1) in set_nums:
                    curr += 1
                    streak += 1 

                max_len = max(max_len, streak)

        return max_len

