class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if (x < 0):
            return False

        xStr = str(x)
        xLen = len(xStr)
        if(xLen == 1):
            return True
        for i in range (xLen//2):
            if (xStr[i]!=xStr[xLen-i-1]):
                return False
        return True

