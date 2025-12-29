class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        s,count,left=sum(arr[0:k]),0,0

        for i in range(k,len(arr)):
            if s/k>=threshold:
                count+=1
            s+=arr[i]
            s-=arr[left]
            left+=1
       
        return count+1 if s/k>=threshold else count