class graph:
    def __init__(self,gdit=None):
        if gdit is None:
            gdit=[]
        self.gdit=gdit
    def getvertices(self):
        return list(self.gdit.values())
    def getedges(self):
        return list(self.gdit.keys())
    #add vertics as a key
    def addvertices(self,vrtx):
        if vrtx not in self.gdit:
            self.gdit[vrtx]=[]

n=int(input())
graph_element={}
for i in range(n):
    k=input('key')
    graph_element[k]=list(input('values').split())
print(graph_element)

g=graph(graph_element)
print(g.getvertices())
print(g.getedges())
s=input('enter the new vertics')
if s:
    g.addvertices(s)
print(graph_element)

