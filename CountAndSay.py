class Solution:
    def countAndSay(self, n):
        string ='1'
        
        #if n == 1:
         #   return "1"
        
        for i in range(n-1):
            temp = ""
            counter = 1
            for j in range(1,len(string)+1):
                if j < len(string) and string[j] == string[j-1]:
                    counter += 1
                else:
                    temp = temp + str(counter) + string[j-1]
                    counter = 1
            string = temp
        return string