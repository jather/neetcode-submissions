class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        recurrence minCost[i] = min((minCost[i-1] + cost[i-1]), minCost[i-2] + cost[i-2]))
        boundary case: minCost[0] = 0
        minCost[1] = 0
        """
        minCost = [0, 0]
        for i in range(2, len(cost) + 1):
            minCost.append(min((minCost[i-1] + cost[i-1]), (minCost[i-2] + cost[i-2])))
        
        return minCost[-1]
        