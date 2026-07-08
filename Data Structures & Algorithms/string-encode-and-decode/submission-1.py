class Solution:

    def encode(self, strs: List[str]) -> str:
        temp = ""

        for i in strs:
            length = len(i)
            temp += str(length) + "," + i
        return temp

    def decode(self, s: str) -> List[str]:
        lst = []
        i = 0

        while i < len(s):
            temp = i
            while s[temp] != ",":
                temp += 1
            length = int(s[i:temp])
            lst.append(s[temp+1:temp+1+length])
            i = temp + 1 + length
        return lst