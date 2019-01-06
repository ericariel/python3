#!/usr/bin/env python
# coding: utf-8

def lengthOfLongestSubstring(s):
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
	print(lengthOfLongestSubstring(s))





