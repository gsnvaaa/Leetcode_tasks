class Solution(object):
    def majorityElement(self, nums):
        from collections import Counter
        counter = Counter(nums)
        max_count, output = 0, 0

        for k, v in counter.items():
            if v > max_count:
                max_count = v
                output = k
        return output