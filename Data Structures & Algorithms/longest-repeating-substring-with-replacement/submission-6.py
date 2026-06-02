class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        maxf = 0
        counts =defaultdict(int)
        r = 0
        longestWindow = 1
        while r < len(s):
            #print(counts)
            v = s[r]
            counts[v]+=1
            if counts[v] > maxf:
                maxf = counts[v]
            
            while (r-l + 1) - maxf >k:
                counts[s[l]] = max( counts[s[l]]-1,0)
                l+=1

            longestWindow = max(longestWindow,r-l + 1)
            r+=1
        return longestWindow