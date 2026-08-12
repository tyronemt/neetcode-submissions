class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = { "(" : ")", "[" : "]", "{" : "}" }

        for c in s:
            if c in dic.keys():
                stack.append(dic[c])
            elif not stack or stack.pop() != c:
                return False

        return len(stack) == 0