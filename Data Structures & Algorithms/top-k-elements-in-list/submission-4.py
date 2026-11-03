class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for i in nums:
            frequency[i] = frequency.get(i, 0) + 1
        bucket = {}
        for key, value in frequency.items():
            bucket[value] = bucket.get(value, [])
            bucket[value].append(key)
        results = []
        for i in range(len(nums), -1, -1):
            if i in bucket:
                results.extend(bucket[i])
                if len(results) == k:
                    return results
        return results