class Solution:
    def romanToInt(self, s):
        dictionary  = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000,"CM":900,"XC":90,"IV":4,"IX":9,"XL":40,"CD":400,"K":1000}
        add = 0
        counter = 0
        for i in range(len(s)):
            if (i+1) == len(s):
                number = dictionary[s[i]] + add
                break
            if dictionary[s[i]] < dictionary[s[i+1]]:
                number = dictionary[s[i]+s[i+1]] + add
                add = number 
                #s = s.replace(s,s[i+2:])
                s= s.replace(s[i+1],"K")
                counter = counter + 1
                if s == "":
                    break
            else:
                number = dictionary[s[i]] + add
                add = number 
        number = number - (counter*1000)
        return number