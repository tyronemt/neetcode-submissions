class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        for c in range(len(s)):
            temp = 1
            for c1 in s[c+1:]:
                if c1 not in s[c : c + temp]:
                    temp += 1
                else:
                    break
            longest = max(longest, temp)
        return longest
