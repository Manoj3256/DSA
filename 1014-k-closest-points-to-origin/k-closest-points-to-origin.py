class Solution(object):
    def kClosest(self, points, k):
        l=len(points)
        a=[]
        b=[]
        t=0,
        for i in range(l):
            t=((points[i][0])**2+(points[i][1])**2)
            a.append([t,i])
        a.sort(reverse=False)
        for i in range(k):
            b.append(points[a[i][1]])
        return b
