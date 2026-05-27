class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortednums = sorted(nums)
        print(sortednums)
        fin = []
        used_trips= set()
        for i, n in enumerate(sortednums):    
            if n >0:
                break
            left = i +1
            right = len(sortednums) -1

            while left < right:
                if sortednums[left] + sortednums[right] + n == 0:
                    print(left,right)
                    if (n,sortednums[left],sortednums[right]) not in used_trips:
                        fin.append([n,sortednums[left],sortednums[right]])
                        used_trips.add((n,sortednums[left],sortednums[right]))
                    left +=1
                    right -=1
                elif sortednums[left] + sortednums[right] + n < 0:
                    left +=1
                elif sortednums[left] + sortednums[right] + n > 0:
                    right -=1
        
        return fin




        