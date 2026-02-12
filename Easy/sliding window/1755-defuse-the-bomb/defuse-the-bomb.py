class Solution(object):
    def decrypt(self, code, k):
        """
        :type code: List[int]
        :type k: int
        :rtype: List[int]
        """
        length=len(code)
        arr=[0]*length
        if k==0:
            return arr
        elif k>0:
            for left in range(length):
                for right in range(1,k+1):
                    arr[left]+=code[(left+right)%length]
        else:
            for left in range(length):    
                for right in range(1,abs(k)+1):
                    arr[left]+=code[(left-right)%length]
        return arr