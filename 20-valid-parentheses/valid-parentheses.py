class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not float(len(s)/2):
            return False
        stack=[]*len(s)
        for i in range(len(s)):
            if s[i]!=")" and s[i]!="}" and s[i]!="]":
                stack.append(s[i])
            elif s[i]==")" :
                if len(stack)>0 and stack.pop()=="(":
                    continue
                else:
                    return False
            elif s[i]=="}" :
                if len(stack)>0 and stack.pop()=="{":
                    continue
                else:
                    return False
            elif s[i]=="]":
                if len(stack)>0 and stack.pop()=="[":
                    continue
                else:
                    return False
        return True if not stack else False

