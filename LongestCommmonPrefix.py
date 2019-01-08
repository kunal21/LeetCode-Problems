class Solution:
    def longestCommonPrefix(self, strs):
        
        if strs == []:
            return ""
        
        shortest = len(strs[0])
        for i in strs:
            if len(i) <= shortest:
                shortest_name = i
        counter = 0

        for char in range(len(shortest_name)):
            for names in range(len(strs)):
                if shortest_name[0:len(shortest_name)] == strs[names][0:len(shortest_name)]:
                    counter = counter + 1
            if counter == len(strs):
                minimum = shortest_name[0:counter+1]
                return minimum
                break
            else:
                counter = 0
                shortest_name = shortest_name[0:len(shortest_name)-1]

        if counter < len(strs):
            return ""