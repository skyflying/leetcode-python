class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        le1=len(nums1)
        le2=len(nums2)
       
        if le1 > le2:
            return self.findMedianSortedArrays(nums2,nums1)
        
        def check(x):
            i=x
            j= (le1+le2+1)//2-i
            if nums1[i-1]<=nums2[j]:
                return True
            return False
        
        def bsurb(l,r):
            while l<r:
                mid =l+r+1 >>1
                if check(mid):
                    l=mid
                else:
                    r = mid -1
            return l
        
        l,r = 0,le1
        i=bsurb(l,r)
        j=(le1+le2+1)//2-i
        left1 = -inf if i == 0 else nums1[i - 1]
        right1 = inf if i == le1 else nums1[i]
        left2 = -inf if j == 0 else nums2[j - 1]
        right2 = inf if j == le2 else nums2[j]
        left,right =max(left1,left2),min(right1,right2)
             
        if  (le1+le2)&1:
            return left
        else:
            return (left+right)/2
        
        
        #i,j分別對應nums1及nums2的分割線
        #i 表示 nums1 分割線左方有 i 個元素，範圍為 0 到 le1
        #j 表示 nums2 分割線左方有 j 個元素，範圍為 0 到 le2
        #分割線左方的元素大於右方，且最多比右方多一個
        # i左方的元素小於等於j右方的元素，且j左方的元素小於等於i右方的元素
        #i,j左方的元素皆取最大，右方元素取最小，兩個取中位數
        #當le1+le2為奇數時，回到左方元素，否則取平均