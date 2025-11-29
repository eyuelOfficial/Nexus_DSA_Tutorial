class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        #get the length of the string 
        stringLength = len(s)
        #this is the flag that we used in it
        found = False
        #this 
        count = 0
        #try to start from the end as it is far more efficent for the code
        for i in range ( stringLength - 1 , -1, -1):
            if(s[i]!=" "):
                count += 1
                found = True
            elif(found):
                break
        return count
        
