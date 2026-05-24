class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        lookup = defaultdict(int)
        for n in nums:
            lookup[n] +=1
        # items = list(lookup.items())

        # sorted_items = sorted(items, key = lambda entry:entry[1] ,reverse= True)
        # fin = []
        # for i in range(k):
        #     fin.append(sorted_items[i][0])
        # return fin
        buckets = [[] for _ in range(len(nums)+1)]
        for key in lookup:
            buckets[lookup[key]].append(key)

        fin = []
        count = 0
        for i in range(len(buckets)-1,-1,-1):
            if buckets[i]:
                for item in buckets[i]:
                    fin.append(item)
                    count+=1
                    if count >= k:
                        return fin
                    
            if count >=k:
                break
        return fin