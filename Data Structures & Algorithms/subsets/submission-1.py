class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            curSubset = []
            for cur in res:
                new = cur.copy()
                new.extend([num])
                curSubset.append(new)
            res.extend(curSubset)
        return res

        