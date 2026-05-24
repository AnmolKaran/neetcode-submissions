class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs: return ""
        fin = []
        for s in strs:
            fin.append(str(len(s)) + ",")
        fin.append("#")
        for s in strs:
            fin.append(s)
        return ''.join(fin)
    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        print(s)
        numCounts = []
        finwords = []
        beforewords = True
        wordind = 0
        i = 0
        
        while s[i]!= "#":
            currNum = ""
            while s[i] != ",":
                currNum += s[i]
                i +=1
            if currNum:
                numCounts.append(int(currNum))
            i+=1
        
        wordind = i+1
        for ct in numCounts:
            finwords.append(s[wordind:wordind+ct])
            wordind +=ct

        return finwords
        

        
