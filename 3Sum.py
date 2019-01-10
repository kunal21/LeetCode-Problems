nums = [-1, 0, 1, 2, -1, -4]
nums = sorted(nums)
final_answer = []
for i in range(len(nums)):
    j = i+1
    k = len(nums)-1
    while(k > j):
        summation = nums[i] + nums[j] + nums[k]
        print(summation)
        if summation > 0:
            k -= 1
        elif summation < 0:
            j += 1
        else:
            answer = [nums[i],nums[j],nums[k]]
            if sorted(answer) not in final_answer:
                final_answer.append(answer)
            j += 1

print(final_answer)





























# final_answer = []
# nums = sorted(nums)
# for i in range(len(nums)):
#     for j in range(i+1,len(nums)):
#         answer = []
#         summation = nums[i] + nums[j]
#         if summation < 0:
#             if int(str(summation)[1:]) in nums[j+1:]:
#                 answer = [nums[i],nums[j],int(str(summation)[1:])]
#                 if sorted(answer) not in final_answer:
#                     final_answer.append(answer)
#         else:
#             if int(("-" + str(summation))) in nums[:i]:
#                 answer = [nums[i],nums[j],int(("-" + str(summation)))]
#                 if sorted(answer) not in final_answer:
#                     final_answer.append(answer)
# print(final_answer)