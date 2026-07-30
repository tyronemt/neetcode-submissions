class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        temp = [0] * 26

        for i in range(len(s)):
            index_s = ord(s[i]) - ord('a')
            index_t = ord(t[i]) - ord('a')

            temp[index_s] += 1
            temp[index_t] -= 1

        for val in temp:
            if val != 0:
                return False
        return True