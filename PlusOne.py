class Solution:
    def plusOne(self, digits):
        sums = ""
        new_list = []
        for i in digits:
            sums = sums + str(i)
        final_ans  = int(sums) + 1
        for i in str(final_ans):
            new_list.append(int(i))
        return new_list