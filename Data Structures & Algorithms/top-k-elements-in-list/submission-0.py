class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = {}

        for num in nums:
            if num not in count_dict:
                count_dict[num] = 1
            else:
                count_dict[num] += 1

        sorted_items = sorted(count_dict.items(), key=lambda x: x[1], reverse=True)

        return [x[0] for x in sorted_items[:k]]
