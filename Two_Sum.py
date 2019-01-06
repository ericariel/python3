#!/usr/bin/env python
# coding: utf-8


class Solution:
#暴力循环解法：
#执行用时: 6280 ms
    def twoSum1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if target==nums[i]+nums[j]:
                    return (i,j)                  
#差值遍历解法：
#执行用时: 1240 ms
    def twoSum2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(0,len(nums)):
            q = target - nums[i]
            if q in nums and nums.index(q)!=i:
                return(i,nums.index(q))             
#哈希表解法：
#执行用时: 48 ms
    def twoSum3(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_table = {}
        for idx, i in enumerate(nums):
            complement = target - i
            if (complement in hash_table):
                return [idx, hash_table[complement]]
            hash_table[i] = idx

if __name__="__main__":
	nums=[1,2,5,8,10]
	target=11
	a=Solution()
	print(a.twoSum1(nums,target))
	print(a.twoSum2(nums,target))
	print(a.twoSum3(nums,target))





# In[ ]:




