class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        # store the length in a variable 
        # then interate till / 2  , we do not need to swap no more 
        # in the iteration we will swap each i indexed and length - 1 - i indexed one (the -1 is cus we will have a zero indexed array mnamn ngr )
        length = len(s)

        for i in range(length/2):
            s[i] , s[length - 1 - i] = s[length - 1 - i] , s[i]
         
