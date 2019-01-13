class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        final_answer = []
        for i in range(len(emails)):
            new_string = (emails[i][:emails[i].index("@")])
            new_string2 = emails[i][:emails[i].index('+')]
            if (new_string2.replace('.',"")) + (emails[i][emails[i].index("@"):]) not in final_answer:
                final_answer.append((new_string2.replace('.',"")) + (emails[i][emails[i].index("@"):]))
        return (len(final_answer))