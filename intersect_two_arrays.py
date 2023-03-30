class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        out=[]   # create an empty list to store the intersection of nums1 and nums2
        n=len(nums1)
        for i in range(n):   # iterate over each element in nums1
            elem=nums1[i]   # get the i-th element of nums1
            if elem in nums2:   # check if the element is present in nums2
                out.append(elem)   # add the element to the output list
                nums2.pop(nums2.index(elem))   # remove the element from nums2
        
        return(out)   # return the intersection of nums1 and nums2 as a list
