class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_list = [0] * 26
        t_list = [0] * 26

        for i in range(len(s)):
            index_s = ord(s[i]) - ord('a')
            index_t = ord(t[i]) - ord('a')

            s_list[index_s] += 1
            t_list[index_t] += 1

        return s_list == t_list