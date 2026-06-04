class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counts = defaultdict(int)
        l = 0
        bestL =l
        bestR = 0
        realCounts = defaultdict(int)
        for c in t:
            realCounts[c] +=1
        if not s or not t or len(t) > len (s):
            return ""
        minLength = 0
        #bestString = deque()
        
        counts[s[0]] = 1
        r = 0
        while r < len(s):
           
            #counts[s[r]] +=1
       
            substringIncluded = True
            for c in t:
                if counts[c] < realCounts[c]:
                    substringIncluded = False
                    break

            while substringIncluded == False:
                
                r +=1
                if r >= len(s):
                    return  s[bestL:bestR+1] if minLength != 0 else ""
                counts[s[r]] +=1
                
                
                substringIncluded = True
                for c in t:
                    if counts[c] < realCounts[c]:
                        substringIncluded = False
                
                
            
            if  minLength == 0 or r- l + 1 < minLength :
                bestL = l
                bestR = r
                minLength = r- l + 1
            
            
            counts[s[l]] -=1
            l+=1
            # print(counts)
            # print()
        return  s[bestL:bestR+1] if minLength != 0 else ""

                
                
            
