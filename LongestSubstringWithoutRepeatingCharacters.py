#!/usr/bin/env python
# coding: utf-8
def lengthOfLongestSubstring1(s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        longest = 0
        sub_s = []
        if l==1:
            return 1
        for x in range(0,l):
            if s[x] in sub_s:
                i = sub_s.index(s[x])+1
                sub_s = sub_s[i:]
            sub_s.append(s[x])
            sub_len = len(sub_s)
            if sub_len > longest:
                longest = sub_len
        return longest
def lengthOfLongestSubstring2(s):
        """
        :type s: str
        :rtype: int
        """
        lists=[]
        ls1=[]
        ls2=[]
        for i in s:
            if i not in ls1:
                ls1.append(i)
            else:
                ls2=ls1[ls1.index(i)+1::]
                lists.append("".join(ls1))
                ls1.clear()
                ls1.extend(ls2)
                ls1.append(i)
        lists.append("".join(ls1))
        k=0
        for list1 in lists:
            if len(list1)>k:
                k=len(list1)
        return k

if __name__ == "__main__":
	s="abac"
	print(lengthOfLongestSubstring1(s))
	print(lengthOfLongestSubstring2(s))





