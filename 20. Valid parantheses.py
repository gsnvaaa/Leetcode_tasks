class Solution(object):
    def isValid(self, s):
        list = {')':'(','}':'{',']':'['}
        stack =[]

        for p in s:
            if p not in list:
                stack.append(p)
            else:
                if not stack:
                    return False
                else:
                    popped = stack.pop()
                    if popped != list[p]:
                        return False
        return not stack  