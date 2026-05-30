class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lastindex = defaultdict(int)
        if not s: return 0
        lst = list(s)
        l = 0
        window = [s[0]]
        longest = 1
        lettersInWindow = set(window)
        for i in range(1, len(s)):
            while s[i] in lettersInWindow:
                l = lastindex[s[i]] + 1
                #r = i + 1
                window = lst[l:i]
                lettersInWindow =  set(window)
            lastindex [s[i]] = i
            window.append(s[i])
            lettersInWindow.add(s[i])
            longest = max(len(window),longest)
        return longest
