class Solution:
    def trap(self, height: List[int]) -> int:
        areaAtPos = [0 for _ in range(len(height))]
        for i in range(len(height)):
            l = None
            r = None
            for ind in range(i,-1,-1):
                if  height[ind] > height[i]:
                    if l :
                        if (height[ind] > height[l]):
                            l = ind
                    else:
                        l = ind
            for ind in range(i+1,len(height)):
                if  height[ind] > height[i]:
                    if r :
                        if (height[ind] > height[r]):
                            r = ind
                    else:
                        r = ind
            if None in [l,r]:
                areaAtPos[i] = 0
            else:
                print(i, height[l],height[r])
                print(min(height[l],height[r]) - height[i])
                print()
                areaAtPos[i] = min(height[l],height[r]) - height[i]
        return sum(areaAtPos)