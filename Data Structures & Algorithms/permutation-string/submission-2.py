class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        chars = Counter(s1)
        for c in set(s2):
            if c not in chars:
                chars[c] = 0
        ogchars = Counter(s2[:len(s1)])
        for c in set(s2):
            if c not in ogchars:
                ogchars[c] = 0
        l = 0
        for r in range(len(s1)-1,len(s2)):
            
            
            print(chars)
            print(ogchars)
            print()
            if set(chars.items()) ==set(ogchars.items()):
                return True
            if r +1 == len(s2):
                return False

            ogchars[s2[r+1]] +=1
            ogchars[s2[l]] -=1
            l+=1
        
        return False