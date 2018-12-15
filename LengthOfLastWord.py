class Solution:
    def lengthOfLastWord(self, s):
        string_new = s[::-1]
        counter = 0
        for i in string_new:
            if i == " " and counter > 0:
                break
            else:
                if i == " ":
                    pass
                else:
                    counter += 1
        return(counter)