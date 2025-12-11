class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        d={}
        j=1
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        
        class minheap():
            def __init__(self):
                self.heap=[]
            def push(self,value):
                self.heap.append(value)
                self.heapify_up(len(self.heap)-1)
            def pop(self):
                if len(self.heap)==1:
                    return self.heap.pop()
                root =self.heap[0]
                self.heap[0]=self.heap.pop()
                self.heapify_down(0)
                return root
            def heapify_up(self,i):
                while i > 0:
                    parent = (i - 1) // 2
                    if self.heap[i] < self.heap[parent]:
                        self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
                        i = parent
                    else:
                        break


            def heapify_down(self,i):
                small=i
                le,ri =2*i+1, 2*i+2
                if le<len(self.heap) and self.heap[le]<self.heap[small]:
                    small=le
                if ri<len(self.heap) and self.heap[ri]<self.heap[small]:
                    small=ri
                if small!= i:
                    self.heap[i],self.heap[small]=self.heap[small],self.heap[i]
                    self.heapify_down(small)
        h=minheap()
        for key,v in d.items():
            h.push([-v,key])
        b=len(h.heap)
        o=[h.pop() for _ in range(b)]
        output = []
        for freq, char in o:
            output.append(char * (-freq))

        return "".join(output)

