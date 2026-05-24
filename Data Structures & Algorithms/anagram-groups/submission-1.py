class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        fin = defaultdict(list)
        aord = ord('a')
        for s in strs:
            charLst = [0 for i in range(26)]
            for char in s:
                ascii_value = ord(char) - aord
                charLst[ascii_value] +=1
            fin[tuple(charLst)].append(s)
        return list(fin.values())

