class Solution:
    def twoSums(self,nums,target):
        dict1={}
        for i in range(len(nums)):
            dict1[nums[i]]=i
        for i in nums:
            for j in dict1:
                if i+j==target:
                    if nums.index(i)!=dict1[j]:
                        return nums.index(i),dict1[j]
                    else:
                        continue
