class Solution:
    def isValid(self, s):
        ls = []
        d = {"(":1,")":1,"{":2,"}":2,"[":3,"]":3}

        if s.count("(") == s.count(")") and s.count("{") == s.count("}") and s.count("[") == s.count("]"):
            for char in s:
                if char == "(" or char == "{" or char == "[":
                    ls.append(char)
                else:
                    if d[(ls.pop())] == d[char]:
                        pass
                    else:
                        return False
                        break
            if ls == []:
                return True
        else:
            return False