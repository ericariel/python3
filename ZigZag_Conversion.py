class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        num=0
        num_change=2*numRows-2
        num_list=[]
        s_list=list(s)
        for i in range(numRows):
            tmp_change=num_change if num_change>=0 else 0
            num=i
            if num==0 or num==numRows-1:
                num_change=2*numRows-2
                while num<len(s):
                    num_list.append(s_list[num])
                    if num_change>0:
                        num+=num_change
                    else:
                        num+=1
            else:
                while num<len(s):
                    num_list.append(s_list[num])
                    num+=num_change
                    num_change=2*numRows-2-num_change    
            num_change=tmp_change-2
        ans="".join(num_list)
        return ans
