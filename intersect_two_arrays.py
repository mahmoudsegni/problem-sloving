class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        out=[]
        for i in range(len(nums1)):
            elem=nums1[i]
            if elem in nums2:
                out.append(elem)
                nums2.pop(nums2.index(elem))
        return(out)