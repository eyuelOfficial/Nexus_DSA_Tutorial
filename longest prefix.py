class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
 freq = []
 numberOfWords = len(strs)
 # the first loop goes through all the elemnts of the of the strings and then makes 
 # to the dict of the code 
 for i in range numberOfWords:
    wordLength = strs[i].length

    for j in range wordLength:
        if strs[i] in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

        
