class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lastindex = defaultdict(int)
        l = 0
        longest = 0
        for i in range(len(s)):
            if s[i] in lastindex and lastindex[s[i]] >= l:
                l = lastindex[s[i]] + 1
            lastindex[s[i]] = i
            longest = max(i - l + 1, longest)
        return longest