class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #for each car, calculate their would-be time at target position. 
        cars = sorted(zip(position, speed), reverse=True)
        stack = []
        for pos, spd in cars:
            time = (target-pos)/spd
            if not stack or time> stack[-1]:
                stack.append(time)

        return len(stack)
