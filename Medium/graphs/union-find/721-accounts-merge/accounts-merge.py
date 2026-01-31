class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        res=[]
        groups,parent,email_name={},{},{}
        def find(x):
            if parent[x]!=x:
                parent[x]=find(parent[x])
            return parent[x]
        def union(x,y):
            ax,ay=find(x),find(y)
            if ax!=ay:
                parent[ay]=ax
        for acc in accounts:
            na,fimail=acc[0],acc[1]
            for i in acc[1:]:
                if i not in parent:
                    parent[i]=i
                email_name[i]=na
                union(fimail, i)
        for a in parent:
            root=find(a)
            groups.setdefault(root,[]).append(a)
        for root,emails in groups.items():
            res.append([email_name[root]]+ sorted(emails))
        return res