class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in ['[','{','(']:
                stack.append(i)
            else:
                if len(stack) == 0:
                  return False
                temp = stack.pop()
                if temp == '[':
                    if i != ']':
                        return False
                if temp == '{':
                    if i != '}':
                        return False
                if temp == '(':
                    if i != ')':
                        return False
        if len(stack) == 0:
            return True
        else:
            return False