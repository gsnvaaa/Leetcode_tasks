class Solution(object):
    def intersection(self, nums1, nums2):
        seen = set(nums1)

        res = []
        for n in nums2:
            if n in seen:
                res.append(n)
                seen.remove(n)
        return res 