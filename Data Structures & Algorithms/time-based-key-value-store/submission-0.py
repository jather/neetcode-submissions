from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.hashmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashmap:
            return ""
        values = self.hashmap[key]
        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2
            if timestamp == values[m][1]:
                return values[m][0]
            if timestamp < values[m][1]:
                r = m - 1
            else:
                l = m + 1
        if r < 0:
            return ""
        else:
            return values[r][0]




        
