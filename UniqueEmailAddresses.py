class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        l = []
        for i in range(len(emails)):
            new_string = (emails[i][:emails[i].index("@")])
            new_string2 = emails[i][:emails[i].index('+')]
            if (new_string2.replace('.',"")) + (emails[i][emails[i].index("@"):]) not in l:
                l.append((new_string2.replace('.',"")) + (emails[i][emails[i].index("@"):]))
        return (len(l))