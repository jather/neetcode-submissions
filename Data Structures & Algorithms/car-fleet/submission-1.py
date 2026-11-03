class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        cars = list(zip(position, speed))
        cars.sort(key=lambda x: x[0])
        print(cars)
        for i in range(0, len(cars)):
            timeLeft = (target - cars[i][0]) / cars[i][1]
            while stack and timeLeft >= stack[-1]:
                stack.pop()
            stack.append(timeLeft)
        return len(stack)


#behind, faster -> merge
# either in front and faster or behind and slower.
# 