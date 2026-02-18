class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p = m + n - 1
        p1 = m - 1
        p2 = n - 1 
         # now we need to loop through the code where we will have the postion of the end and go through them 
         # till we reach the end of the p1 , where the len is m + n 
        while p1 >= 0 and p2 >= 0 :
            if nums1[p1] >  nums2[p2]:
                nums1[p] = nums1[p1] 
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1 
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1
