#leetcode
#link=https://leetcode.com/problems/median-of-two-sorted-arrays/description/
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        new =sorted(nums1+nums2)
        n=len(new)
        mid=(n//2)
        
        if((n%2) == 0):
        	return((new[mid-1]+new[mid])/2)
        else:
        	return(float(new[mid]))